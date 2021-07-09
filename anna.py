import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit 
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_cmd():
    try:
        with sr.Microphone() as source:
            print('Listening......')
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if 'anna' in cmd:
                cmd = cmd.replace('anna','') 
                print(cmd)
                
    except:
        pass 
    return cmd

def run_anna():
    cmd = take_cmd()
    print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in cmd:
        time = datetime.datetime.now().strftime('%I %M %p')
        talk('Current time is' + time)
    elif 'search' in cmd:
        person = cmd.replace('search','')
        talk('searching' + person)
        info = wikipedia.summary(person,1)
        talk(info)
        print(info)
    elif 'joke' in cmd:
        talk('telling a joke now')
        talk(pyjokes.get_joke())
    else:
        talk('cant understand what you saying')
        
while True:        
    run_anna()
