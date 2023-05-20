# Copyright (c) 2023 Colin Pannikkat, Ajinkya Gokule, Sarvesh Thiruppathi, David Gesl
# Shorts Generator

from video import Video
from editor import captionedVideo
from audio import textToSpeech

def main():
    # get video type from user
    videoType = input("Enter desired background video type: ")
    video = Video(videoType)
    video.saveVideo()

    # get caption string
    captionString = "Richard Feynman said, “Never confuse education with intelligence, you can have a PhD and still be an idiot.” What are some real life examples of this? My professor, a brilliant neurosurgeon, once decided to directly smell a bottle of ammonia. He then told me “don't smell that”. I did not plan to! Me. Masters in cybersecurity and can't help my 5th grader with his math homework. My ex wife with a PhD in neuroscience driving my car around with the handbrake on calling me to ask about the noise and smell. I had a professor for higher mathematics who had real difficulties figuring out how to extract a cup of coffee from the vending machine. Bless him. I work with medical doctors all the time for work. Doctors are some of the dumbest smart people I have ever met."

    # get autio file
    audioFile = textToSpeech(captionString)

    # apply caption to video
    inputVideo = video.filename
    savedVideo = captionedVideo(inputVideo, captionString, audioFile)

    print("Video saved as:", savedVideo, "in captionVideos folder")

if __name__ == "__main__":
    main()