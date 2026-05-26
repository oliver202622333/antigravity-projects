
import os
import sys
from pathlib import Path

VIDEO_PATH = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile\产品设计中心20260521周列会.mp4"
OUTPUT_DIR = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile"

def transcribe_video_directly(video_path):
    try:
        import whisper
        print("正在加载 Whisper 模型...")
        model = whisper.load_model("base")
        print("正在转录视频...")
        result = model.transcribe(video_path, language="zh")
        return result["text"], result.get("segments", [])
    except Exception as e:
        print(f"直接转录失败: {e}")
        return None, None

def generate_minutes_with_content(transcript, segments, output_path):
    segments_text = ""
    if segments:
        segments_text = "\n\n## 详细时间线\n"
        for seg in segments:
            start = seg.get("start", 0)
            end = seg.get("end", 0)
            text = seg.get("text", "")
            segments_text += f"\n[{start:.1f}s - {end:.1f}s] {text}"

    template = f"""# 产品设计中心20260521周列会会议纪要

## 会议信息
- **日期**: 2026年5月21日
- **参会人员**: 产品设计中心团队
- **记录人**: AI助手

## 会议内容摘要
{transcript[:500] if transcript else '(内容待补充)'}...

## 讨论内容

### 主要议题
{transcript if transcript else '(待补充)'}

## 决议事项
-

## 待办事项
| 任务 | 负责人 | 截止日期 | 状态 |
|------|--------|----------|------|
|      |        |          |      |

## 下次会议安排
-

---

## 完整录音转写
{transcript if transcript else '(待补充)'}
{segments_text}
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(template)
    print(f"会议纪要已生成: {output_path}")

def main():
    print("=== 会议内容处理 ===")

    video_path = Path(VIDEO_PATH)
    if not video_path.exists():
        print(f"错误: 视频文件不存在: {VIDEO_PATH}")
        return

    minutes_path = Path(OUTPUT_DIR) / (video_path.stem + "_会议纪要.md")

    print(f"\n处理视频: {video_path.name}")
    print("这可能需要几分钟时间...")

    transcript, segments = transcribe_video_directly(str(video_path))

    if transcript:
        print("\n转录完成!")
        generate_minutes_with_content(transcript, segments, str(minutes_path))
    else:
        print("\n转录失败，请检查是否需要安装FFmpeg")
        print("FFmpeg 下载: https://ffmpeg.org/download.html")

if __name__ == "__main__":
    main()

