from pytube import YouTube

from yt_dlp import YoutubeDL

download_option = input("Do you want to download this video? (yes/no): ").lower()

if download_option == "yes":
    url = 'https://youtu.be/SBGnSPL6p9o?si=u9BFjydp4cun-z_t'
    ydl_opts = {'format': 'best'}
    with YoutubeDL(ydl_opts) as ydl:
        print("Downloading...")
        ydl.download([url])
        print("Download completed.")
else:
    print("Download aborted.")