from gtts import gTTS

def textToSpeech(captionString):
    speech = gTTS(text=captionString, lang='en')
    speech.save("./audio/textToSpeech.mp3")
    return "./audio/textToSpeech.mp3"