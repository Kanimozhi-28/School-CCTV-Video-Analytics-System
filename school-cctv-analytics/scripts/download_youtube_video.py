import os

def download_video(url, output_path):
    # Use yt-dlp or similar to download
    print(f"Downloading {url} to {output_path}")
    # os.system(f"yt-dlp -o {output_path} {url}")

if __name__ == "__main__":
    download_video("https://youtube.com/sample", "data/videos/sample.mp4")
