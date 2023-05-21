from gtts import gTTS

def textToSpeech(captionString):
    speech = gTTS(text=captionString, lang='en')
    speech.save("./audio/audioFiles/textToSpeech.mp3")
    return "./audio/audioFiles/textToSpeech.mp3"