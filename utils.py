# pip install instaloader
import instaloader
import os
import shutil


async def video_downloader(username):
    d = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(d.context, username)

    for n, post in enumerate(profile.get_posts()):
        if post.is_video:
            d.download_post(post, target=f"video{n}")
    return d.close()


async def scaner_folders():
    folders = os.scandir()

    video_folders = []
    result = []

    for f in folders:
        if f.name.startswith("video"):
            video_folders.append(f.name)

    for item in video_folders:
        folder = os.scandir(item)

        for i in folder:
            if i.name.endswith(".mp4"):
                result.append(
                    f"{item}/{i.name}"
                )
    
    return result


async def delete_folders():
    folders = os.scandir()

    for f in folders:
        if f.name.startswith("video"):
            shutil.rmtree(f.name)
