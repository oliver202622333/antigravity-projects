
import os
import sys
from pathlib import Path
import numpy as np

AUDIO_PATH = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile\产品设计中心20260521周列会.wav"
OUTPUT_DIR = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile"

print("正在加载 Whisper...")
import whisper

print("正在加载完整WAV...")
import wave
with wave.open(AUDIO_PATH, 'rb') as wf:
    n_channels = wf.getnchannels()
    framerate = wf.getframerate()
    n_frames = wf.getnframes()
    audio_bytes = wf.readframes(n_frames)

print(f"音频长度: {n_frames / framerate:.1f} 秒")

audio_int16 = np.frombuffer(audio_bytes, dtype=np.int16)
audio_float32 = audio_int16.astype(np.float32) / 32768.0

if n_channels == 2:
    audio_float32 = audio_float32.reshape(-1, 2).mean(axis=1)

print("正在加载模型...")
model = whisper.load_model("small")

print("\n正在完整转录... (这可能需要较长时间)")
result = model.transcribe(
    audio_float32,
    language="zh",
    fp16=False,
    verbose=True,
    word_timestamps=False,
    temperature=0.0
)

print("\n=== 转录完成 ===")
print(f"总文本长度: {len(result.get('text', ''))} 字符")

transcript = result.get("text", "")
segments = result.get("segments", [])

# 生成时间线
segments_md = ""
for seg in segments:
    start = seg.get("start", 0)
    end = seg.get("end", 0)
    text = seg.get("text", "").strip()
    if text:
        m, s = divmod(int(start), 60)
        em, es = divmod(int(end), 60)
        segments_md += f"\n[{m:02d}:{s:02d}-{em:02d}:{es:02d}] {text}"

minutes_path = Path(OUTPUT_DIR) / "产品设计中心20260521周列会_会议纪要.md"
content = f"""# 产品设计中心20260521周列会会议纪要

## 会议信息
- **日期**: 2026年5月21日
- **会议类型**: 产品设计中心周例会

## 会议内容摘要

{transcript[:800]}...

## 会议完整记录

{transcript}

---

## 会议时间线

{segments_md}
"""

with open(minutes_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\n会议纪要已保存: {minutes_path}")
print("\n前1000字符预览:")
print("-" * 60)
print(content[:1000])
print("...")

