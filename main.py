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
        print('Clearing background noises...')
        engine.say("Clearing background noises...")
        engine.runAndWait()
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me something...')
        engine.say("Ask me something...")
        engine.runAndWait()
        recorded_audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(recorded_audio, language='en-US')
        text = text.lower()
        print('Your message: ', format(text))
    except:
        pass
    if 'google' in text:
        webbrowser.open('www.google.com')
        engine.say('Opening Google')
        engine.runAndWait()
    elif 'time' in text:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        engine.say(current_time)
        engine.runAndWait()
    elif 'play' in text:
        pywhatkit.playonyt(text)
        engine.say('Playing ' + text)
        engine.runAndWait()
    elif 'youtube' in text:
        webbrowser.open('www.youtube.com')
        engine.say('Opening YouTube')
        engine.runAndWait()
    elif 'bye' in text:
        engine.say('See you later')
        engine.runAndWait()
        exit()
while True:
    cmd()
