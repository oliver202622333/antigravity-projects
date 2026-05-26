
import os
import sys
from pathlib import Path
import numpy as np

VIDEO_PATH = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile\产品设计中心20260521周列会.mp4"
OUTPUT_DIR = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile"

def load_audio_from_wav(wav_path):
    import wave
    with wave.open(wav_path, 'rb') as wav_file:
        n_channels = wav_file.getnchannels()
        sampwidth = wav_file.getsampwidth()
        framerate = wav_file.getframerate()
        n_frames = wav_file.getnframes()

        audio_data = wav_file.readframes(n_frames)
        audio_array = np.frombuffer(audio_data, dtype=np.int16)
        audio_array = audio_array.astype(np.float32) / 32768.0

        return audio_array, framerate

def transcribe_audio_data(audio_array, sample_rate):
    try:
        import whisper
    except ImportError:
        print("请先安装: pip install openai-whisper")
        return None

    print("正在加载 Whisper 模型...")
    model = whisper.load_model("base")

    # 重采样到16000Hz
    if sample_rate != 16000:
        try:
            import scipy.signal
            print(f"重采样 {sample_rate}Hz -> 16000Hz...")
            number_of_samples = round(len(audio_array) * 16000 / sample_rate)
            audio_array = scipy.signal.resample(audio_array, number_of_samples)
        except:
            pass

    print("正在转录...")
    result = model.transcribe(
        audio_array,
        language="zh",
        fp16=False,
        verbose=True
    )
    return result

def save_minutes(result, output_path):
    transcript = result.get("text", "")
    segments = result.get("segments", [])

    segments_md = ""
    for seg in segments:
        start = seg.get("start", 0)
        text = seg.get("text", "").strip()
        if text:
            m, s = divmod(int(start), 60)
            segments_md += f"\n[{m:02d}:{s:02d}] {text}"

    content = f"""# 产品设计中心20260521周列会会议纪要

## 会议信息
- **日期**: 2026年5月21日
- **会议类型**: 产品设计中心周例会

## 会议内容摘要
{transcript[:500]}...

## 会议完整记录

{transcript}

---

## 详细时间线
{segments_md}
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n会议纪要已保存: {output_path}")

def main():
    print("=== 会议纪要生成 ===\n")

    audio_path = Path(OUTPUT_DIR) / "产品设计中心20260521周列会.wav"
    if not audio_path.exists():
        print(f"音频文件不存在: {audio_path}")
        return

    print("正在加载音频...")
    audio_array, sample_rate = load_audio_from_wav(str(audio_path))
    print(f"音频加载完成: {len(audio_array)} samples, {sample_rate}Hz")

    print("\n开始语音识别...")
    result = transcribe_audio_data(audio_array, sample_rate)

    if result:
        minutes_path = Path(OUTPUT_DIR) / "产品设计中心20260521周列会_会议纪要.md"
        save_minutes(result, str(minutes_path))
    else:
        print("转录失败")

if __name__ == "__main__":
    main()

