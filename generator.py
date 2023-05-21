# Copyright (c) 2023 Colin Pannikkat, Ajinkya Gokule, Sarvesh Thiruppathi, David Gesl
# Shorts Generator

from video.video import Video
from editor.editor import captionedVideo, generate_video
from audio.audio import textToSpeech
from content.chatGPT import generate_req
import content.reddit as reddit
import os
from random import randrange

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t\t\tWelcome to Shorts Generator!"
          "\n\tThis program will generate a short video with the content of your choice."
          "\n-------------------------------------------------------------------------------------"
          "\nCopyright (c) 2023 Colin Pannikkat, Ajinkya Gokule, Sarvesh Thiruppathi, David Gesl"
          "\n-------------------------------------------------------------------------------------\n")
    
    # get caption string
    userChoice = input("Choose where to get content from:"
                       "\n(1) AskReddit"
                       "\n(2) ChatGPT"
                       "\n(3) Generate a completely random video\n:")
    while(userChoice != "1" and userChoice != "2" and userChoice != "3"):
        userChoice = input("Invalid input. Please try again: ")
    if userChoice == "1":
        captionString = reddit.main()
    elif userChoice == "2": 
        prompt = input("Enter a prompt for chatGPT: ")
        captionString = generate_req(prompt, 500)
    elif userChoice == "3": # generate random video
        prompts = ["Generate a random AITA story under 150 words", #0
                   "Generate a random AskReddit question and responses under 150 words", #1
                   "Generate a random story under 150 words", #2
                   "Explain some mathematical concept under 150 words"] #3
        captionString = generate_req(prompts[randrange(0,3)], 200) # randomly generates a reddit story
        video = Video("short gameplay footage for tiktok video") # looks for general background video
        video.saveVideo(len(captionString)) # scrapes video from youtube
        inputVideo = "./video/" + video.filename # gets video path
        savedVideo = generate_video(inputVideo, captionString) # applies caption to video
        print("Video saved at:", savedVideo) # prints video path
        quit()

    # get video type from user
    videoType = input("Enter desired background video type: ")
    video = Video(videoType)
    video.saveVideo(len(captionString))

    # get autio file
    # audioFile = textToSpeech(captionString)

    # apply caption to video
    inputVideo = "./video/" + video.filename
    savedVideo = generate_video(inputVideo, captionString)

    print("Video saved at:", savedVideo)

if __name__ == "__main__":
    main()