
import os
import sys
from pathlib import Path

VIDEO_PATH = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile\产品设计中心20260521周列会.mp4"
AUDIO_PATH = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile\产品设计中心20260521周列会.wav"
OUTPUT_DIR = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile"

print("正在加载 Whisper...")
import whisper
import numpy as np

print("正在尝试直接加载WAV...")

# 手动读取WAV
import wave
with wave.open(AUDIO_PATH, 'rb') as wf:
    n_channels = wf.getnchannels()
    sampwidth = wf.getsampwidth()
    framerate = wf.getframerate()
    n_frames = wf.getnframes()
    audio_bytes = wf.readframes(n_frames)

print(f"读取WAV: {n_frames} frames, {framerate}Hz")

# 转换为numpy
audio_int16 = np.frombuffer(audio_bytes, dtype=np.int16)
audio_float32 = audio_int16.astype(np.float32) / 32768.0

# 如果是立体声，转单声道
if n_channels == 2:
    audio_float32 = audio_float32.reshape(-1, 2).mean(axis=1)

# 如果采样率不对，重采样
if framerate != 16000:
    print(f"重采样 {framerate}Hz -> 16000Hz...")
    try:
        import scipy.signal
        num_samples = int(len(audio_float32) * 16000 / framerate)
        audio_float32 = scipy.signal.resample(audio_float32, num_samples)
    except ImportError:
        print("未安装scipy，尝试使用原始采样率")

print(f"音频数据 shape: {audio_float32.shape}")

print("\n正在加载模型...")
model = whisper.load_model("base")

print("\n开始转录...")
# 使用模型的直接方法
mel = whisper.log_mel_spectrogram(audio_float32).to(model.device)
options = whisper.DecodingOptions(language="zh", fp16=False)
result = whisper.decode(model, mel, options)

print("\n=== 转录结果 ===")
print(result.text)

# 保存结果
minutes_path = Path(OUTPUT_DIR) / "产品设计中心20260521周列会_会议纪要.md"
content = f"""# 产品设计中心20260521周列会会议纪要

## 会议信息
- **日期**: 2026年5月21日
- **会议类型**: 产品设计中心周例会

## 会议记录

{result.text}
"""

with open(minutes_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\n会议纪要已保存: {minutes_path}")

