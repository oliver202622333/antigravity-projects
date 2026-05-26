
import os
import sys
import subprocess
from pathlib import Path
import json

VIDEO_PATH = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile\产品设计中心20260521周列会.mp4"
OUTPUT_DIR = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile"
SCRIPT_DIR = Path(__file__).parent

def find_ffmpeg():
    possible_paths = []
    if (SCRIPT_DIR / "ffmpeg_path.txt").exists():
        with open(SCRIPT_DIR / "ffmpeg_path.txt") as f:
            path = f.read().strip()
            if Path(path).exists():
                return path

    for path in os.environ.get("PATH", "").split(os.pathsep):
        ffmpeg_exe = Path(path) / "ffmpeg.exe"
        if ffmpeg_exe.exists():
            return str(ffmpeg_exe)

    return None

def extract_audio_with_ffmpeg(video_path, audio_output_path, ffmpeg_path):
    cmd = [
        ffmpeg_path,
        "-i", video_path,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "64k",
        "-ar", "16000",
        "-ac", "1",
        "-y",
        audio_output_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        return True
    else:
        print(f"FFmpeg错误: {result.stderr}")
        return False

def transcribe_audio(audio_path):
    try:
        import whisper
        print("正在加载 Whisper 模型 (small)...")
        model = whisper.load_model("small")
        print("正在转录...")
        result = model.transcribe(audio_path, language="zh", verbose=True)
        return result
    except Exception as e:
        print(f"转录错误: {e}")
        return None

def generate_structured_minutes(result, output_path):
    transcript = result.get("text", "")
    segments = result.get("segments", [])

    segments_md = ""
    for seg in segments:
        start = seg.get("start", 0)
        end = seg.get("end", 0)
        text = seg.get("text", "").strip()
        if text:
            m, s = divmod(int(start), 60)
            segments_md += f"\n[{m:02d}:{s:02d}] {text}"

    minutes = f"""# 产品设计中心20260521周列会会议纪要

## 会议信息
- **日期**: 2026年5月21日
- **会议类型**: 产品设计中心周例会
- **记录人**: AI助手

## 会议内容概要

{transcript[:800]}...

## 讨论要点

（基于会议录音整理）

{transcript}

## 行动项

| 事项 | 负责人 | 截止时间 | 状态 |
|------|--------|----------|------|
|      |        |          |      |

## 下次会议

- 时间：待定
- 议题：待定

---

## 会议录音详细记录

{segments_md}
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(minutes)
    print(f"\n会议纪要已生成: {output_path}")

def main():
    print("=== 会议纪要生成器 ===\n")

    ffmpeg_path = find_ffmpeg()
    if not ffmpeg_path:
        print("未找到 FFmpeg")
        print("请按以下步骤操作：")
        print("1. 下载 FFmpeg: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip")
        print("2. 解压，找到 bin/ffmpeg.exe")
        print("3. 将其路径写入: e:\\Oliver\\my_ant_projects\\ffmpeg_path.txt")
        return

    print(f"使用 FFmpeg: {ffmpeg_path}")

    video_path = Path(VIDEO_PATH)
    if not video_path.exists():
        print(f"视频不存在: {video_path}")
        return

    audio_path = Path(OUTPUT_DIR) / (video_path.stem + ".mp3")
    minutes_path = Path(OUTPUT_DIR) / (video_path.stem + "_会议纪要.md")

    if not audio_path.exists():
        print("\n正在提取音频...")
        if not extract_audio_with_ffmpeg(str(video_path), str(audio_path), ffmpeg_path):
            print("音频提取失败")
            return
        print(f"音频已保存: {audio_path}")
    else:
        print(f"音频已存在: {audio_path}")

    print("\n开始语音识别 (这可能需要几分钟)...")
    result = transcribe_audio(str(audio_path))

    if result:
        generate_structured_minutes(result, str(minutes_path))
    else:
        print("转录失败")

if __name__ == "__main__":
    main()

