#https://towardsdatascience.com/building-a-simple-voice-assistant-for-your-mac-in-python-62247543b626
import speech_recognition as sr
import os


r = sr.Recognizer()
mic = sr.Microphone()


def activate(phrase='mama'):
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            transcript = r.recognize_google(audio)
            if transcript.lower() == phrase:
                return True
            else:
                return False
    except:
        print("Something went wrong")



while True:
    if activate() == True:
        try:
            print("Hey Kyle, how can I help you today?")
            with mic as source:
                print("Say Something!")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                transcript = r.recognize_google(audio)
                print(transcript)
        except:
            pass
    else:
        pass


