from moviepy.editor import *

filename = "video2.mp4"
audioDuration = 40
partitions = 8
captionString = "Richard Feynman said, “Never confuse education with intelligence, you can have a PhD and still be an idiot.” What are some real life examples of this? My professor, a brilliant neurosurgeon, once decided to directly smell a bottle of ammonia. He then told me “don't smell that”. I did not plan to! Me. Masters in cybersecurity and can't help my 5th grader with his math homework. My ex wife with a PhD in neuroscience driving my car around with the handbrake on calling me to ask about the noise and smell. I had a professor for higher mathematics who had real difficulties figuring out how to extract a cup of coffee from the vending machine. Bless him. I work with medical doctors all the time for work. Doctors are some of the dumbest smart people I have ever met."

clip = VideoFileClip(f'rawVideos/{filename}')

clip = clip.subclip(0, audioDuration)
if(clip.w > clip.h):
    clip = clip.crop(x_center=clip.w/2, y_center=clip.h/2, width=(clip.h) * 9/16, height=clip.h)

# splits the caption string into partitions
def textClipArray(captionString, partitions):
    textClipArray = []
    for i in range(partitions):
        textClipArray.append(
            TextClip(
            captionString[i*len(captionString)//partitions:(i+1)*len(captionString)//partitions], 
            color='white',
            # stroke_color='white',
            # stroke_width=clip.h * 0.02 * 0.005,
            method='caption',
            size=(clip.w * 0.9,None),
            align='center',
            font='Verdana-Bold',
            fontsize=clip.h * 0.025,
            bg_color='transparent',
            ).on_color(color=(0,0,0), col_opacity=0.8).set_duration(audioDuration/partitions).set_start(i*audioDuration/partitions).set_pos((0.05,0.15), relative=True))
    return textClipArray

texts = textClipArray(captionString, partitions)
texts.insert(0,clip)
# overlay the text clips onto the video
CompositeVideoClip(texts).write_videofile(f'./captionedVideos/{filename}', codec='libx264', fps=24)
# print(TextClip.search('Bold','font'))
# print(TextClip.list('color'))

def captionedVideo(clipPath, captionString, audioPath):
    clip = VideoFileClip(clipPath)
    audio = AudioFileClip(audioPath)
    audioDuration = int(audio.duration)
    clip = clip.subclip(0, audioDuration)
    if(clip.w > clip.h):
        clip = clip.crop(x_center=clip.w/2, y_center=clip.h/2, width=(clip.h) * 9/16, height=clip.h)
    