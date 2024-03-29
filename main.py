from pytube import YouTube, Playlist
import pyfiglet
import termcolor
import os
import datetime
from os import name

def clear_screen():
    if name == "nt":
        return os.system("cls")
    else:
        return os.system("clear")

clear_screen()
print(termcolor.colored(pyfiglet.figlet_format("YT.DOWNLOADER"), color="red"))
print(termcolor.colored("-" * 80, color="blue"))

print(termcolor.colored("Version:  => ", color="red"), end=" ")
print(termcolor.colored("1.0", color="yellow"))
print(end="\n")
print(termcolor.colored("Design By: ", color="red"), end=" ")
print(termcolor.colored("Mano!", color="yellow"))
print(end="\n")
print("_" * 100)
print("_" * 100)
print(termcolor.colored(datetime.datetime.now().strftime("%a, %d %B %Y, %H:%M:%S"), color="blue"))
print("_" * 100)
print("_" * 100)


save_path = input(
    termcolor.colored("Enter your path to save videos: ", color="blue")
).strip()
# clear_screen()


def main():
    url = input(
        termcolor.colored("Enter Youtube Url Video or Playlist: ", color="red")
    ).strip()
    # clear_screen()

    if "playlist" in url.lower():
        download_playlist(url)
    else:
        download_video(url)


def download_video(url):
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()

    print(termcolor.colored("Downloading..", color="green"), video.title)
    stream.download(save_path)
    print(termcolor.colored("Download Completed!", color="green"))
    # clear_screen()


def download_playlist(url):
    playList = Playlist(url)
    total_video = len(playList)
    counter = 0

    print(termcolor.colored("Total Videos is: ", color="blue"),": ", termcolor.colored(total_video, color="grey"))

    for video in playList.video_urls:
        yt = YouTube(video)

        stream = yt.streams.get_highest_resolution()

        print(termcolor.colored("Downloading: ", color="green"), termcolor.colored(yt.title, color="grey"))
        stream.download(save_path)

        counter += 1

        print(termcolor.colored(f'{counter}/{total_video}', color="yellow"))

    print(termcolor.colored("Download Completed!", color="green"))



if __name__ == "__main__":
    main()
