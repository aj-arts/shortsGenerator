from moviepy.editor import *
from audio import textToSpeech

captionString = "AITA for refusing to lend my car to my sister for her road trip and potentially ruining her plans? I (26F) recently splurged on a luxurious new car with the money I've been saving for years. My sister (24F) begged me to borrow it for a week-long road trip with her friends, claiming it would be a once-in-a-lifetime experience. However, I firmly declined, explaining that I didn't trust her driving skills and was afraid of potential accidents or damage. She exploded, accusing me of being selfish and unsupportive of her dreams. Our family got involved, with some siding with me and others berating me for being overly possessive of my possessions. Now she's left scrambling for alternative transportation and her friends are upset too. So, am I truly the asshole for prioritizing my car's safety and my peace of mind over potentially ruining my sister's dream road trip? Or should I have been more supportive and trusting, putting her happiness above my concerns?"

# captionString = "1812 AITA for cutting off my friend after they revealed they were involved in an affair? I (30F) recently found out that my close friend (28F) had been engaging in a long-term affair with a married man. I was devastated and couldn't believe that she would betray someone's trust in such a way. I decided to cut off all contact with her, refusing to even hear her side of the story. Some people in our mutual friend group are calling me heartless and judgmental, saying that I should have been more understanding and supportive. They argue that everyone makes mistakes and deserves a second chance. However, I strongly believe that cheating is a breach of integrity and loyalty. Am I the asshole for severing ties with my friend and refusing to give her another chance, or am I justified in setting boundaries and distancing myself from someone who would engage in such deceitful behavior?"

def textClipArray(captionString, partitions, audioDuration, width, height):
    textClipArray = []
    for i in range(partitions):
        textClipArray.append(
            TextClip(
            captionString[i*len(captionString)//partitions:(i+1)*len(captionString)//partitions], 
            color='white',
            # stroke_color='white',
            # stroke_width=clip.h * 0.02 * 0.005,
            method='caption',
            size=(width * 0.9,None),
            align='center',
            font='Verdana-Bold',
            fontsize=height * 0.025,
            bg_color='transparent',
            ).on_color(color=(0,0,0), col_opacity=0.8).set_duration(audioDuration/partitions).set_start(i*audioDuration/partitions).set_pos((0.05,0.15), relative=True))
    return textClipArray

def captionedVideo(clipPath, captionString, audioPath):
    clip = VideoFileClip(clipPath)
    audio = AudioFileClip(audioPath).fx(vfx.speedx, 1.3)
    audioDuration = int(audio.duration)
    clip = clip.subclip(0, audioDuration)
    if(clip.w > clip.h):
        clip = clip.crop(x_center=clip.w/2, y_center=clip.h/2, width=(clip.h) * 9/16, height=clip.h)
    partitions = 8
    texts = textClipArray(captionString, partitions, audioDuration, clip.w, clip.h)
    texts.insert(0,clip)
    clip.audio = audio
    CompositeVideoClip(texts).write_videofile(f'./captionedVideos/video1.mp4', codec='libx264', fps=24, audio_codec='aac', verbose=False,logger=None)
    return f'./captionedVideos/video1.mp4'

captionedVideo('./rawVideos/video2.mp4', captionString, textToSpeech(captionString))