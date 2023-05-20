from gtts import gTTS

def textToSpeech(captionString):
    speech = gTTS(text=captionString, lang='en')
    speech.save("audioFiles/textToSpeech.mp3")
    return "audioFiles/textToSpeech.mp3"