# Copyright (c) 2023 Colin Pannikkat, Ajinkya Gokule, Sarvesh Thiruppathi, David Gesl
# Shorts Generator

from video.video import Video
from editor.editor import captionedVideo
from audio.audio import textToSpeech
import reddit.reddit as reddit
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t\t\tWelcome to Shorts Generator!"
          "\n\tThis program will generate a short video with a story of your choice."
          "\n-------------------------------------------------------------------------------------"
          "\nCopyright (c) 2023 Colin Pannikkat, Ajinkya Gokule, Sarvesh Thiruppathi, David Gesl"
          "\n-------------------------------------------------------------------------------------\n")
    # get video type from user
    videoType = input("Enter desired background video type: ")
    video = Video(videoType)
    video.saveVideo()

    # get caption string
    captionString = reddit.main()
    # get autio file
    audioFile = textToSpeech(captionString)

    # apply caption to video
    inputVideo = "./video/rawVideos/" + video.filename
    savedVideo = captionedVideo(inputVideo, captionString, audioFile)

    print("Video saved at:", savedVideo)

if __name__ == "__main__":
    main()