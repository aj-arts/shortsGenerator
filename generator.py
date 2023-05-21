# Copyright (c) 2023 Colin Pannikkat, Ajinkya Gokule, Sarvesh Thiruppathi, David Gesl
# Shorts Generator

from video.video import Video
from editor.editor import captionedVideo, generate_video
from audio.audio import textToSpeech
from content.chatGPT import generate_req
from content.reddit import main as reddit
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t\t\tWelcome to Shorts Generator!"
          "\n\tThis program will generate a short video with the content of your choice."
          "\n-------------------------------------------------------------------------------------"
          "\nCopyright (c) 2023 Colin Pannikkat, Ajinkya Gokule, Sarvesh Thiruppathi, David Gesl"
          "\n-------------------------------------------------------------------------------------\n")
    
    # get caption string
    print("Choose whether to get content from AskReddit or chatGPT.")
    userChoice = input("Enter 1 for AskReddit or 2 for chatGPT: ")
    while(userChoice != "1" and userChoice != "2"):
        userChoice = input("Invalid input. Please try again: ")
    if userChoice == "1":
        captionString = reddit()
    elif userChoice == "2": 
        prompt = input("Enter a prompt for chatGPT: ")
        captionString = generate_req(prompt, 500)  
        
    captionLength = len(captionString)

    # get video type from user
    videoType = input("Enter desired background video type: ")
    video = Video(videoType)
    video.saveVideo(captionLength)

    # get autio file
    # audioFile = textToSpeech(captionString)

    # apply caption to video
    inputVideo = "./video/" + video.filename
    savedVideo = generate_video(inputVideo, captionString)

    print("Video saved at:", savedVideo)

if __name__ == "__main__":
    main()