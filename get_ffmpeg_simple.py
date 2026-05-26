
import os
import sys
import urllib.request
import zipfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
FFMPEG_DIR = SCRIPT_DIR / "ffmpeg_bin"
FFMPEG_DIR.mkdir(exist_ok=True)

# 使用更精简的 FFmpeg 版本
FFMPEG_URL = "https://github.com/eugeneware/ffmpeg-static/releases/download/b4.4/win32-x64.zip"

def download_and_extract():
    zip_path = FFMPEG_DIR / "ffmpeg.zip"

    if not zip_path.exists():
        print("正在下载 FFmpeg...")
        try:
            urllib.request.urlretrieve(FFMPEG_URL, zip_path)
        except:
            print("备用下载源...")
            # 备用源
            FFMPEG_URL2 = "https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-7.0.1-essentials_build.zip"
            try:
                urllib.request.urlretrieve(FFMPEG_URL2, zip_path)
            except Exception as e:
                print(f"下载失败: {e}")
                return False

    print("正在解压...")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(FFMPEG_DIR)
    except:
        pass

    ffmpeg_exe = None
    for root, dirs, files in os.walk(FFMPEG_DIR):
        for file in files:
            if file.lower() == "ffmpeg.exe":
                ffmpeg_exe = Path(root) / file
                break
        if ffmpeg_exe:
            break

    if ffmpeg_exe:
        with open(SCRIPT_DIR / "ffmpeg_path.txt", "w") as f:
            f.write(str(ffmpeg_exe))
        print(f"FFmpeg 已保存: {ffmpeg_exe}")
        return True

    return False

if __name__ == "__main__":
    success = download_and_extract()
    if success:
        print("\nFFmpeg 准备就绪!")
    else:
        print("\n请手动下载:")
        print("https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip")

