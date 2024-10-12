import pyttsx3
def speak(talk):
    engine = pyttsx3.init("sapi5")
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    if len(voices) > 3:
        engine.setProperty('voice', voices[3].id)
    else:
        engine.setProperty('voice', voices[1].id)  # Use the first available voice
    engine.say(talk)
    engine.runAndWait()