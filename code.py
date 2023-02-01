
from ast import main
from time import time
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import sys
import pywhatkit as pyw
import tkinter 
hour=int(datetime.datetime.now().hour)
minu=int(datetime.datetime.now().minute)
minu=minu+1
engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("good morning aman")
    elif hour>=12 and hour<17:
        speak("good afternoon aman")
    elif hour>=17 and hour<=24:
        speak("good evening aman")

    speak("hi i am max please tell me how may i help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("recognising...")
        query = r.recognize_google(audio,language="en-in")
        print("user said -", query)
    except Exception as e:
        #print(e)
        print("say that again please...")
        return "none"
    return query


wishme()
while True:
    query = takecommand().lower()
    
    
    #logic for implemting query
    
    if "wikipedia" in query:
        speak("searching wikipedia... please wait")
        query=query.replace("can you tell me about", " ")
        query=query.replace("according to wikipedia", " ")
        results = wikipedia.summary(query,sentences=1)
        speak("according to wikipedia")
        print(results)
        speak(results)
        
        
    elif "open youtube" in query:
        chrome=webbrowser.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        chrome.open_new("youtube.com")
    
    elif "open netflix" in query:
        chrome=webbrowser.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        chrome.open_new("netflix.com")


    elif "play music" in query:
        music_dir = "C:\\Users\\amans\\OneDrive\\Desktop\\music"
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[random.randrange(0,len(songs))]))
    
    
    elif "time" in query:
        strTime=datetime.datetime.now().strftime("%H:%m:%S")
        speak(f"sir the time right now is {strTime}")
        
    elif "code" in query:
        chromepath="C:\\Users\\amans\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(chromepath)
        
        
    elif "whatsapp" in query:
        phonebook ={"papa" : "+919891920402" , "pooja" : "+9199891920404" , "mummy":"9891920403 "}
        speak("to whom do you want to send the message sir")
        a=takecommand().lower()
        speak("whats the message sir")
        b=takecommand()
        c=phonebook[a]
        
        pyw.sendwhatmsg(c,b,hour,minu)
        
    elif "exit" in query:
        sys.exit()
