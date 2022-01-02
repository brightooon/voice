import ssl
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
#import ecapture #for taking photos
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from bs4 import BeautifulSoup
from urllib.request import urlopen
import Quartz

engine = pyttsx3.init('sap15')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
urname = ""

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
        print("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
        print('Good Afternoon Sir')
    else:
        speak("Good Evening Sir")
        print("Good Evening Sir")
    speak("I'm your assistant")

def takeCommand():
    listener = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source)
    
    try:
        print("Listening..")
        query = listener.recognize_google(audio, language = 'en-in')
        print(f"User: {query}\n")
    except:
        print(Exception)
        print("Unable to recognize")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('ur email id', 'ur email password')
    server.sendemail('ur email id', to, content)
    server.close()

def username():
    speak("Your name Sir")
    urname = takeCommand()
    speak("Welcome Mister")
    speak(urname)
    columns = shutil.get_terminal_size().columns
    print("Welcome Mr.", urname.center(columns))
    speak(f"How can I help u {urname}")


if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    print('loading voice assistant ~~~')
    speak('loading your voice assistant')
    wishMe()
    username()
    while True:
        query = takeCommand().lower()
        if query is None:
            speak("say exit or quit if you want to quit voice assistance")
            continue
        if "quit" in query or "exit" in query:
            speak("voice assistance shutting down")
            print("voice assistance shutting down")
            exit()
        if "google" in query:
            speak("google opened")
            webbrowser.open("https://www.google.com/")
            time.sleep(3)
        elif "wikipedia" in query or "wiki" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
            print(result)
        elif "youtube" in query:
            speak("youtube opened")
            webbrowser("https://www.youtube.com/")
            time.sleep(3)
        elif "time now" in query:
            stringtime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"time is {stringtime} now")
        elif  "spotify" in query:
            speak("spotify opened")
            os.system("open -a Spotify")
            time.sleep(3)
        elif "telegram" in query:
            speak("telegram opened")
            os.system("open -a Telegram")
            time.sleep(3)
        elif "news" in query:
            speak("news today")
            webbrowser.open_new_tab("https://www.nbcnews.com/")
            time.sleep(3)
        elif "translate" in query:
            speak("try to do translate here")
            webbrowser.open_new_tab("https://translate.google.com/")
            time.sleep(3)
        elif "mail" in query or "send a mail" in query:
            try:
                speak("what you want to send")
                content = takeCommand()
                speak("Who you are sending to")
                to = input()
                sendEmail(to, content)
                speak("Email sent")
            except:
                print(Exception)
                speak("not able to send email")
        elif "joke" in query:
            speak(pyjokes.get_joke())
        elif "search" in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(3)
        elif "calculator" in query:
            speak("Say what you want to calculate")
            question = takeCommand()
            client = wolframalpha.Client("G9RP66-JHTL7RGXX2")
            result = client.query(question)
            answer = next(result.results).text
            speak("The answer is " + answer)
            print("The answer is" + answer)
        elif "v s code" in query:
            speak("v s code opened")
            os.system("open Downloads/VisualStudioCode.app")
            time.sleep(3)
        elif "x code" in query:
            speak("x code opened")
            os.system("open -a Xcode")
            time.sleep(3)
        elif "bash" in query or "bin" in query or "terminal" in query:
            speak("terminal opened")
            os.system("open -a Terminal")
            time.sleep(3)
        elif "stop" in query or "stop listening" in query or "stop now" in query:
            speak("how long you want to stop voice assisitance from listening")
            stoptime = int(takeCommand())
            time.sleep(stoptime)
            print(f"stop for {stoptime} sec")
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            webbrowser.open_new_tab("https://www.google.nl/maps/place" + location + "")
            speak(f"{location} is located")
            time.sleep(3)
        elif "python" in query or "test in python" in query or "test python" in query:
            speak("open python runner")
            os.system("open -a PyCharm")
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif "log off" in query or "sign out" in query:
            speak("will be sign out in ten seconds and please exit all the applications")
            subprocess.call(["shutdown", "/l"])
        elif "lock screen" in query or "lock off" in query or "lock down" in query:
            speak("lock now")
            d = Quartz.CGSessionCopyCurrentDictionary()
            print('CGSSessionScreenIsLocked' in d.keys())
        elif "weather" in query:
            weatherapi = "ur weather api in openweathermap"
            speak("What's the city name")
            city_name = takeCommand()
            url = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + weatherapi
            res = requests.get(url)
            response = res.json()
            if response["cod"] != "404":
                wea = response["weather"]
                description = wea[0]["description"]
                main = response["main"]
                temp = main["temp"]
                pressure = main["pressure"]
                humidity = main["humidity"]
                speak(f"{city_name} is {description} today")
                print(f"{city_name} is {description} today")
                speak(f"temperaturue is {temp} in kelvin unit")
                print(f"temperaturue is {temp} in kelvin unit")
                speak(f"humidity is {humidity} percent")
                print(f"humidity is {humidity} percent")
            else:
                message = response["message"]
                speak(message)
                print(message)
        elif "send message" in query:
            # we use twilo for sending message
            acsid = "ACe55f64ab4251e4918203c3ac19221845"
            authtoken = " ur auth token"
            client = Client(acsid, authtoken)
            speak("what you want to send")
            try:
                message = client.messages \
                    .create(body = takeCommand(), me = "+19252851277", to = "+19252851277")
                print(message.sid)
                speak("message delivered")
            except:
                speak("failed to send message")
        elif "take note" in query or "take a note" in query or "write note" in query or "write a note" in query:
            speak("What shouid i write")
            note = takeCommand()
            file = open("voiceassistance.txt", "w")
            speak("Do you want me include date and time")
            boole  = takeCommand()
            if "yes" in boole or "sure" in boole or "of course" in boole or "yea" in boole:
                stringtime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(stringtime)
                file.write(":- \n")
            file.write(note)
        elif "show" in query and "note" in query:
            speak("showing note")
            file = open("voiceassistance.txt", "r")
            print(file.read())
            speak(file.read())
