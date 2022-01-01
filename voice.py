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
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clients.textui import progress
from bs4 import BeautifulSoup
#import win32com.client as wincl
from urllib.request import urlopen


engine = pyttsx3.init('sap15')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

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
    server = smtplib.SMTP('smtp.gamil.com', 587)
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