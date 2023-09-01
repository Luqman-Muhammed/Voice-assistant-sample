import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
recognizer = sr.Recognizer()


def cmd():

    global text
    with sr.Microphone() as source:
        print('Clearing..... bg noises')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me....')
        recordedaudio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(recordedaudio, language='en_US')
        text = text.lower()
        print('Your message: ', format(text))

    except:
        pass

    if 'google' in text:
        a = 'opening google...'
        engine.say(a)
        engine.runAndWait()
        webbrowser.open('www.google.com')
    if 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    if 'play' in text:
        b = 'Opening youtube...'
        engine.say(b)
        engine.runAndWait()
        pywhatkit.playonyt(text)
    if 'youtube' in text:
        c = 'Opening youtube...'
        engine.say(c)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
    if 'bye' in text:
        d = 'see you later'
        engine.say(d)
        engine.runAndWait()


while True:
    cmd()

