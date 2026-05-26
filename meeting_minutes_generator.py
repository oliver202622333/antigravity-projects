
import os
import sys
import subprocess
from pathlib import Path

VIDEO_PATH = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile\产品设计中心20260521周列会.mp4"
OUTPUT_DIR = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile"

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def extract_audio(video_path, output_audio_path):
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "128k",
        "-ar", "44100",
        "-y",
        output_audio_path
    ]
    subprocess.run(cmd, check=True)
    print(f"音频已提取到: {output_audio_path}")

def transcribe_audio(audio_path):
    print("正在尝试语音识别...")
    print("注意: 需要安装语音识别库如 openai-whisper 或使用 API 服务")
    print("请选择:")
    print("1. 使用本地 Whisper 模型 (需先安装: pip install openai-whisper)")
    print("2. 使用其他语音识别服务")
    print("3. 先生成空模板，稍后手动输入内容")

    choice = input("请输入选项 (1-3): ").strip()

    if choice == "1":
        try:
            import whisper
            print("正在加载 Whisper 模型...")
            model = whisper.load_model("base")
            print("正在转录音频...")
            result = model.transcribe(audio_path, language="zh")
            return result["text"]
        except ImportError:
            print("Whisper 未安装，请运行: pip install openai-whisper")
            return None
    elif choice == "3":
        return ""
    else:
        return None

def generate_meeting_minutes(transcript, output_path):
    template = f"""# 产品设计中心20260521周列会会议纪要

## 会议信息
- **日期**: 2026年5月21日
- **参会人员**:
- **记录人**:

## 会议议程
1.

## 讨论内容

### 议题一
-

### 议题二
-

## 决议事项
-

## 待办事项
| 任务 | 负责人 | 截止日期 | 状态 |
|------|--------|----------|------|
|      |        |          |      |

## 下次会议安排
-

---

*原始录音转写内容:*
{transcript if transcript else '(待补充)'}
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(template)
    print(f"会议纪要已生成: {output_path}")

def main():
    print("=== 会议纪要生成工具 ===")

    if not check_ffmpeg():
        print("错误: 未找到 ffmpeg，请先安装 ffmpeg 并添加到系统 PATH")
        print("下载地址: https://ffmpeg.org/download.html")
        return

    video_path = Path(VIDEO_PATH)
    if not video_path.exists():
        print(f"错误: 视频文件不存在: {VIDEO_PATH}")
        return

    audio_path = Path(OUTPUT_DIR) / (video_path.stem + ".mp3")
    minutes_path = Path(OUTPUT_DIR) / (video_path.stem + "_会议纪要.md")

    print(f"\n处理视频: {video_path.name}")

    if not audio_path.exists():
        print("\n步骤1: 从视频中提取音频...")
        extract_audio(str(video_path), str(audio_path))
    else:
        print(f"\n音频文件已存在: {audio_path}")

    transcript = None
    if minutes_path.exists():
        print(f"\n会议纪要已存在: {minutes_path}")
        overwrite = input("是否覆盖? (y/n): ").strip().lower()
        if overwrite != "y":
            print("已取消")
            return

    print("\n步骤2: 语音识别...")
    transcript = transcribe_audio(str(audio_path))

    print("\n步骤3: 生成会议纪要...")
    generate_meeting_minutes(transcript, str(minutes_path))

    print("\n完成!")

if __name__ == "__main__":
    main()

