# Written by: Colin Pannikkat
# Date: 05/21/2023

from pytube import Search
from pytube.extract import is_age_restricted
from datetime import datetime

class Video:
    '''
    Video scraper using PyTube to download desired background videos from YouTube

    Attributes
    ----------
        videoType (str): type of video to search for
        usedVideos (str): file containing used videos
        search (Search): search object from pytube
            access search results with search.results
        tries (int): number of tries to find video
        now (datetime): current date and time
        datetimestr (str): current date and time as string
        filename (str): filename of video

    Usage
    -------
        video = Video(videoType)
            Initialize video object
        video.saveVideo()
            Finds and saves video with type requirements to rawVideos folder
    '''

    def __init__ (self, videoType):
        '''
        Initialize video object

        Parameters
        ----------
            videoType (str): type of video to search for
        
        Raises
        ------
            Exception: No video type specified
        '''        
        
        self.videoType = videoType
        if self.videoType == None or self.videoType == "":
            raise Exception("No video type specified")
        self.usedVideos = "./video/used_videos.txt" # file containing used videos
        self.search = Search(self.videoType) # search youtube for video type
        self.tries = 0 # number of tries to find video
        self.now = datetime.now()
        self.datetimestr = self.now.strftime("%m-%d-%H:%M")
        self.filename = None

    def saveVideo(self, captionLength):
        '''
        Finds video within video type and length requirements 
        and saves video to rawVideos folder

        Parameters
        ----------
            captionLength (int): length of caption in characters
        '''

        self.captionLength = captionLength
        captionTime = self.captionLength/11.75 # convert caption length (in chars) to seconds

        def checkVideo():
            '''
            Checks if video has already been used
            '''

            usedVideos = open(self.usedVideos, 'r')
            if videoTitle in usedVideos.read():
                return True
            else:
                return False
        
        for i in self.search.results:
            videoTitle = str(i.title)
            if not is_age_restricted(i.watch_html) and captionTime <= i.length <= 300 and not checkVideo(): # checks if video is between 1 and 5 minutes
                print("Found:", videoTitle) 
                
                # if video has not been used, download it    
                try:
                    print("Downloading video...")
                    try:
                        videoType = self.videoType.replace(" ", "_") # replace spaces with underscores
                        self.filename = "backgroundvideo.mp4"
                        i.streams.filter(file_extension='mp4', res='720p').first().download(filename=self.filename, output_path="./video/")
                    except Exception as e:
                        raise e
                    else:   
                        print("Video downloaded successfully!")
                    # write video to used videos file
                    usedVideos = open(self.usedVideos, mode="a")
                    usedVideos.write(i.title + "\n")
                    usedVideos.close()
                    return
                except Exception as e:
                    print(str(e))
                    continue
            else:  
                continue
        print("No video's found in lookup, expanding search...")
        self.search.get_next_results() # expand search
        self.tries += 1
        if self.tries == 10:
            print("No video's found in lookup after 10 tries, exiting...")
            return
        self.saveVideo(captionLength)