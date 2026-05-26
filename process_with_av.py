
import os
import sys
import tempfile
from pathlib import Path
import numpy as np

VIDEO_PATH = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile\产品设计中心20260521周列会.mp4"
OUTPUT_DIR = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile"

def extract_audio_with_pyav(video_path, output_wav_path):
    try:
        import av
    except ImportError:
        print("请先安装: pip install av")
        return False

    print("正在打开视频文件...")
    try:
        container = av.open(video_path)
        audio_stream = next(s for s in container.streams if s.type == 'audio')

        print("正在提取音频...")
        resampler = av.AudioResampler(
            format='s16',
            layout='mono',
            rate=16000
        )

        audio_frames = []
        for frame in container.decode(audio_stream):
            frame.pts = None
            out_frames = resampler.resample(frame)
            for out_frame in out_frames:
                audio_frames.append(out_frame.to_ndarray())

        if audio_frames:
            audio_data = np.concatenate(audio_frames, axis=1)
            audio_data = audio_data.flatten()

            print(f"正在保存 WAV...")
            import wave
            with wave.open(output_wav_path, 'wb') as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(2)
                wav_file.setframerate(16000)
                wav_file.writeframes(audio_data.astype(np.int16).tobytes())

            return True
        return False
    except Exception as e:
        print(f"提取音频失败: {e}")
        return False

def transcribe_audio(audio_path):
    try:
        import whisper
        print("正在加载 Whisper 模型...")
        model = whisper.load_model("base")
        print("正在转录...")
        result = model.transcribe(audio_path, language="zh", fp16=False, verbose=True)
        return result
    except Exception as e:
        print(f"转录失败: {e}")
        return None

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

## 会议内容

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

    video_path = Path(VIDEO_PATH)
    if not video_path.exists():
        print(f"视频不存在: {video_path}")
        return

    audio_path = Path(OUTPUT_DIR) / (video_path.stem + ".wav")
    minutes_path = Path(OUTPUT_DIR) / (video_path.stem + "_会议纪要.md")

    if not audio_path.exists():
        print("步骤1: 提取音频...")
        if not extract_audio_with_pyav(str(video_path), str(audio_path)):
            print("音频提取失败")
            return
        print(f"音频已保存: {audio_path}")
    else:
        print(f"音频已存在: {audio_path}")

    print("\n步骤2: 语音识别...")
    result = transcribe_audio(str(audio_path))

    if result:
        print("\n步骤3: 生成会议纪要...")
        save_minutes(result, str(minutes_path))
    else:
        print("转录失败")

if __name__ == "__main__":
    main()

