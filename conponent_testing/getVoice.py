'''
Testing speech recognition and synthesis.
If everything is installed correctly,
this file will wait for you to say something
and then repeat back what it hears.
'''


#library for speech recognition.  It's a wrapper for Google's APIs.
#pip install SpeechRecognition
import speech_recognition as sr

#library for text to speech
#pip install pyttsx3
#https://pypi.org/project/pyttsx3/
import pyttsx3
engine = pyttsx3.init()


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print "Say something!"
    audio = r.listen(source)


try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    voice_text = r.recognize_google(audio)
    print "Google Speech Recognition thinks you said " + voice_text
    engine.say(voice_text)
    engine.runAndWait()
except sr.UnknownValueError:
    print "Google Speech Recognition could not understand audio"
except sr.RequestError as e:
    print "Could not request results from Google Speech Recognition service; {0}".format(e)
