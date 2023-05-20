from moviepy.editor import *

filename = "video1.mov"
audioDuration = 40
partitions = 4
captionString = "Richard Feynman said, “Never confuse education with intelligence, you can have a PhD and still be an idiot.” What are some real life examples of this? My professor, a brilliant neurosurgeon, once decided to directly smell a bottle of ammonia. He then told me “don't smell that”. I did not plan to! Me. Masters in cybersecurity and can't help my 5th grader with his math homework. My ex wife with a PhD in neuroscience driving my car around with the handbrake on calling me to ask about the noise and smell. I had a professor for higher mathematics who had real difficulties figuring out how to extract a cup of coffee from the vending machine. Bless him. I work with medical doctors all the time for work. Doctors are some of the dumbest smart people I have ever met."

clip = VideoFileClip(f'rawVideos/{filename}')
print(clip)

# print the caption string into 4 parts

# def textClipArray(captionString, partitions):
#     textClipArray = []
#     for i in range(partitions):
#         textClipArray.append(
#             TextClip(
#             captionString[i*len(captionString)//partitions:(i+1)*len(captionString)//partitions], 
#             color='white', 
#             stroke_color='black',
#             stroke_width=0.5,
#             method='caption',
#             size=(clip.w,clip.h/4),
#             align='center',
#             ).set_duration(audioDuration/partitions).set_start(i*audioDuration/partitions))
#     return textClipArray

# print(textClipArray(captionString, partitions))