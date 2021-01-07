import speech_recognition as sp
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sp.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sp.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is'+time)
    elif 'open' in command:
        file = command.replace('open','')
        talk('Opening '+file)
    elif 'wiki' in command:
        serch = command.replace('wikki','')
        info = wikipedia.summary(serch, 1)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'sleep' in command:
        engine.stop()
    else:
        talk('I didn\'t get you rrepeat again')

while True:
    run_alexa()