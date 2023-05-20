from gtts import gTTS

def textToSpeech(captionString):
    speech = gTTS(text=captionString, lang='en')
    speech.save("audioFiles/textToSpeech.mp3")
    return "audioFiles/textToSpeech.mp3"

textToSpeech("Richard Feynman said, “Never confuse education with intelligence, you can have a PhD and still be an idiot.” What are some real life examples of this? My professor, a brilliant neurosurgeon, once decided to directly smell a bottle of ammonia. He then told me “don't smell that”. I did not plan to! Me. Masters in cybersecurity and can't help my 5th grader with his math homework. My ex wife with a PhD in neuroscience driving my car around with the handbrake on calling me to ask about the noise and smell. I had a professor for higher mathematics who had real difficulties figuring out how to extract a cup of coffee from the vending machine. Bless him. I work with medical doctors all the time for work. Doctors are some of the dumbest smart people I have ever met.")