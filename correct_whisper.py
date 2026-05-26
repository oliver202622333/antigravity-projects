
import os
import sys
from pathlib import Path
import numpy as np

AUDIO_PATH = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile\产品设计中心20260521周列会.wav"
OUTPUT_DIR = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile"

print("正在加载 Whisper...")
import whisper

print("正在加载WAV...")
import wave
with wave.open(AUDIO_PATH, 'rb') as wf:
    n_channels = wf.getnchannels()
    sampwidth = wf.getsampwidth()
    framerate = wf.getframerate()
    n_frames = wf.getnframes()
    audio_bytes = wf.readframes(n_frames)

audio_int16 = np.frombuffer(audio_bytes, dtype=np.int16)
audio_float32 = audio_int16.astype(np.float32) / 32768.0

if n_channels == 2:
    audio_float32 = audio_float32.reshape(-1, 2).mean(axis=1)

# 使用whisper的pad_or_trim方法
print("正在处理音频...")
model = whisper.load_model("base")

# 直接使用whisper的音频处理
audio = whisper.pad_or_trim(audio_float32)

print("正在转录...")
result = model.transcribe(
    audio,
    language="zh",
    fp16=False,
    verbose=True,
    without_timestamps=False
)

print("\n=== 完成 ===")
print(f"转录文本长度: {len(result.get('text', ''))}")

transcript = result.get("text", "")
segments = result.get("segments", [])

segments_md = ""
for seg in segments:
    start = seg.get("start", 0)
    text = seg.get("text", "").strip()
    if text:
        m, s = divmod(int(start), 60)
        segments_md += f"\n[{m:02d}:{s:02d}] {text}"

minutes_path = Path(OUTPUT_DIR) / "产品设计中心20260521周列会_会议纪要.md"
content = f"""# 产品设计中心20260521周列会会议纪要

## 会议信息
- **日期**: 2026年5月21日
- **会议类型**: 产品设计中心周例会

## 会议内容

{transcript}

---

## 详细时间线

{segments_md}
"""

with open(minutes_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\n会议纪要已保存到: {minutes_path}")
print("\n文件内容预览:")
print("-" * 50)
print(content[:500])
print("...")

