from videoScraper.video import Video

def main():
    # get video type from user
    videoType = input("Enter desired background video type: ")
    video = Video(videoType)
    video.saveVideo()

if __name__ == "__main__":
    main()