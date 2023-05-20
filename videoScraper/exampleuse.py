from video import Video

# get video type from user
videoType = input("Enter desired background video type: ")
video = Video(videoType)
video.saveVideo()