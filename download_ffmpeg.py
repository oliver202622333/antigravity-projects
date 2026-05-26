
import os
import sys
import urllib.request
import zipfile
import subprocess
from pathlib import Path

FFMPEG_URL = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
SCRIPT_DIR = Path(__file__).parent
FFMPEG_ZIP = SCRIPT_DIR / "ffmpeg.zip"
FFMPEG_DIR = SCRIPT_DIR / "ffmpeg"

def download_ffmpeg():
    print("正在下载 FFmpeg...")
    try:
        urllib.request.urlretrieve(FFMPEG_URL, FFMPEG_ZIP)
        print("下载完成")
        return True
    except Exception as e:
        print(f"下载失败: {e}")
        return False

def extract_ffmpeg():
    print("正在解压 FFmpeg...")
    try:
        with zipfile.ZipFile(FFMPEG_ZIP, 'r') as zip_ref:
            zip_ref.extractall(FFMPEG_DIR)
        print("解压完成")
        return True
    except Exception as e:
        print(f"解压失败: {e}")
        return False

def find_ffmpeg_exe():
    for root, dirs, files in os.walk(FFMPEG_DIR):
        if "ffmpeg.exe" in files:
            return Path(root) / "ffmpeg.exe"
    return None

def main():
    print("=== FFmpeg 安装工具 ===")

    if not FFMPEG_ZIP.exists():
        if not download_ffmpeg():
            print("下载失败，请手动下载 FFmpeg")
            print("下载地址: https://github.com/BtbN/FFmpeg-Builds/releases")
            return

    if not FFMPEG_DIR.exists():
        if not extract_ffmpeg():
            return

    ffmpeg_exe = find_ffmpeg_exe()
    if ffmpeg_exe:
        print(f"\n找到 FFmpeg: {ffmpeg_exe}")
        with open(SCRIPT_DIR / "ffmpeg_path.txt", "w") as f:
            f.write(str(ffmpeg_exe))
        print("路径已保存到 ffmpeg_path.txt")
    else:
        print("未找到 ffmpeg.exe")

if __name__ == "__main__":
    main()

