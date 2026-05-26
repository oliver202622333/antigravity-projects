
import os
import sys
from pathlib import Path

VIDEO_PATH = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile\产品设计中心20260521周列会.mp4"
OUTPUT_DIR = r"C:\Users\Administrator\AppData\Roaming\NCIMPC\CacheFiles\VideoFile"

try:
    import whisper
    print("Whisper 已加载")

    print("\n正在尝试直接加载视频...")
    model = whisper.load_model("base")

    print("开始转录 (尝试直接读取视频文件)...")
    try:
        result = model.transcribe(VIDEO_PATH, language="zh", fp16=False)
        print("转录成功!")

        transcript = result.get("text", "")
        segments = result.get("segments", [])

        minutes_path = Path(OUTPUT_DIR) / "产品设计中心20260521周列会_会议纪要.md"

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

## 会议记录

{transcript}

---

## 时间线记录
{segments_md}
"""

        with open(minutes_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"\n成功! 会议纪要已保存到: {minutes_path}")

    except Exception as e:
        print(f"需要FFmpeg来处理视频文件。")
        print(f"\n请按以下步骤操作：")
        print(f"1. 下载 FFmpeg: https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z")
        print(f"2. 解压到文件夹")
        print(f"3. 将 bin 文件夹添加到系统环境变量 PATH")
        print(f"4. 重新运行此脚本")

except ImportError:
    print("请先安装: pip install openai-whisper")

