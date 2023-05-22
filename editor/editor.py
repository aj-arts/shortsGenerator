from moviepy.editor import *
from gtts import gTTS

captionString = "Hey there, remember those epic videos that hooked you in? The ones where a snappy bot read out the juiciest Reddit recaps, while jaw-dropping Minecraft parkour unfolded in the background? Admit it, you had no reason to watch, but you couldn't tear your eyes away. Well, get ready for this mind-blowing revelation: brace yourself, because those videos were probably whipped up by AI. Yeah, you heard me right! Even my voice chatting with you right now? AI-generated. The captions you're devouring? AI-generated. And get this, the entire video was scraped right off the internet, all thanks to AI, without any human intervention whatsoever. Isn't that mind-blowing? I mean, c'mon, I had your undivided attention from start to finish. Keep watching to find out how we did it."

# def textClipArray(captionString, partitions, audioDuration, width, height):
#     textClipArray = []
#     for i in range(partitions):
#         textClipArray.append(
#             TextClip(
#             captionString[i*len(captionString)//partitions:(i+1)*len(captionString)//partitions], 
#             color='white',
#             stroke_color='black',
#             stroke_width=height * 0.02 * 0.06,
#             method='caption',
#             size=(width * 0.9,None),
#             align='center',
#             font='Verdana-Bold',
#             fontsize=height * 0.03,
#             bg_color='transparent',
#             )
#             .on_color(color=(0,0,0), col_opacity=0.8)
#             .set_duration(audioDuration/partitions)
#             .set_start(i*audioDuration/partitions)
#             .set_pos((0.05,0.15), relative=True))
#     return textClipArray

# def captionedVideo(clipPath, captionString, audioPath):
#     clip = VideoFileClip(clipPath)
#     audio = AudioFileClip(audioPath).fx(vfx.speedx, 1.3)
#     audioDuration = int(audio.duration)
#     clip = clip.subclip(0, audioDuration)
#     if(clip.w > clip.h):
#         clip = clip.crop(x_center=clip.w/2, y_center=clip.h/2, width=(clip.h) * 9/16, height=clip.h)
#     partitions = audioDuration//5
#     texts = textClipArray(captionString, partitions, audioDuration, clip.w, clip.h)
#     texts.insert(0,clip)
#     clip.audio = audio
#     CompositeVideoClip(texts).write_videofile(f'./video/video.mp4', codec='libx264', fps=24, audio_codec='aac', logger=None)
#     return f'./video/video.mp4'

# define a function that takes in a string breaks it into single words and returns a list of words
def break_into_words(captionString):
    words = captionString.split()
    return words

# define a function that takes in a string breaks punctuation into account and returns a list of sentences
def break_into_sentences(captionString):
    sentences = []
    sentence = ""
    for i in range(len(captionString)):
        if captionString[i] == "?" or captionString[i] == "!" or captionString[i]==".":
            sentence += captionString[i]
            sentences.append(sentence)
            sentence = ""
        else:
            sentence += captionString[i]
    # print(sentences)

    # for sentence in sentences:
    #     if sentence == '.' or sentences == '!' or sentences == '?':
    #         sentences.remove(sentence)
    # print(sentences)

    return sentences

# define a function that takes in a list of words converts them to speech and returns a list of audio clips
def sentencesToAudioList(words):
    audio_clips = []
    for i in range(len(words)):
        try:
            gTTS(text=words[i], lang='en').save(f'./audio/{i}.mp3')
            audio_clips.append(AudioFileClip(f'./audio/{i}.mp3').fx(vfx.speedx, 1.3))
        except Exception as e:
            print(str(e), "Error in generating audio with", words[i])
    return audio_clips

# define a function that generates a video from captionString
def generate_video(clipPath, captionString):
    print("Adding captions to video...")
    clip = VideoFileClip(clipPath)
    if (clip.w > clip.h):
        clip = clip.crop(x_center=clip.w/2, y_center=clip.h/2, width=(clip.h) * 9/16, height=clip.h)
    captionList = break_into_sentences(captionString)
    audioList = sentencesToAudioList(captionList)
    totalDuration = 0
    for i in range(len(captionList)):
        audioList[i] = audioList[i].set_start(totalDuration)

        captionList[i] = TextClip(
            captionList[i],
            color='white',
            stroke_color='black',
            stroke_width=clip.h * 0.04 * 0.05,
            method='caption',
            size=(clip.w,None),
            align='center',
            font='Impact',
            fontsize=clip.h * 0.04,
            bg_color='transparent',
            ).set_duration(audioList[i].duration).set_start(totalDuration).set_pos('center')

        totalDuration += audioList[i].duration
    combinedAudio = CompositeAudioClip(audioList)
    clip.audio = combinedAudio
    clip = clip.subclip(0, totalDuration)
    CompositeVideoClip([clip] + captionList).write_videofile(f'./video/video.mp4', codec='mpeg4', fps=24, audio_codec='aac', logger=None)
    return f'./video/video.mp4'

#print(TextClip.search('Impact','font'))
# generate_video('./video/backgroundvideo.mp4', captionString)