from videoScraper.video import Video
from editor import videoEditor

def main():
    # get video type from user
    videoType = input("Enter desired background video type: ")
    video = Video(videoType)
    video.saveVideo()

    # apply caption to video
    inputVideo = video.filename
    savedVideo = videoEditor(inputVideo, captionString, audioFile)

    print("Video saved as:", savedVideo, "in captionVideos folder")

if __name__ == "__main__":
    main()