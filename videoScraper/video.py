from pytube import Search

class Video:

    def __init__ (self, videoType):
        
        self.videoType = videoType
        self.usedVideos = "./videoScraper/used_videos.txt" # file containing used videos
        self.search = Search(self.videoType) # search youtube for video type
        self.tries = 0 # number of tries to find video

    # tries and find video within length requirements
    def saveVideo(self):
        
        # check if video has already been used
        def checkVideo():
            usedVideos = open(self.usedVideos, 'r')
            if videoTitle in usedVideos.read():
                return True
            else:
                return False
        
        for i in self.search.results:
            videoTitle = str(i.title)
            if 30 <= i.length <= 300 and not checkVideo(): # checks if video is between 30 seconds and 5 minutes
                print("Found:", videoTitle) 
                
                # if video has not been used, download it    
                try:
                    print("Downloading video...")
                    i.streams.filter(file_extension='mp4', res='720p').first().download(output_path="./rawVideos/")
                    print("Video downloaded successfully!")
                    # write video to used videos file
                    usedVideos = open(self.usedVideos, mode="a")
                    usedVideos.write(i.title + "\n")
                    usedVideos.close()
                    return
                except:
                    print("Error downloading video, trying another...")
                    continue
            else:  
                continue
        print("No video's found in lookup, expanding search...")
        self.search.get_next_results()
        self.tries += 1
        if self.tries == 10:
            print("No video's found in lookup after 10 tries, exiting...")
            return
        self.saveVideo()