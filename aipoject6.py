# -*- coding: utf-8 -*-


import pyttsx3
import speech_recognition as sr
import subprocess
import tkinter
import json
import random
import operator
import datetime
import webbrowser
import os
#from gtts import gTTS
#import winshell
#import pyjokes
#import feedparser
import smtplib
#import ctypes
import time
import requests
#import wolframalpha
#from clint.textui import progress
import win32com.client as wincl
from urllib.request import urlopen
import shutil
import pyaudio
import africastalking

africastalking.initialize(
    username='API_USERNAME',
    api_key='API_KEY',
)
message = "Thank you for booking an Appointment with us.",
phone = "+254792050576",
sms = africastalking.SMS



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon ")
    else:
        speak("Good Evening")
        
    assname=("Jane")
    speak("I am your Assistant")
    speak(assname)
    speak("How can i help you")
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to recognize your voice.")
        speak("Unable to recognize your voice.")
        return "None"
    return query

    
if __name__ =='__main__':
    clear=lambda: os.system('cls')
    
    clear()
    wishMe()

    
    while True:
        query=takeCommand().lower()
        
        if 'hello' in query:
            speak('hello, I am Jane your booking asssistant')
            speak('how may I help you?')
        elif 'book an appointment' in query:
           speak('which department?')
        elif 'optical' in query:
            speak('okay..')
            speak('what is your name')
            uname=takeCommand()
            speak('Welcome to blue hospital')
            speak(uname)
            speak('time available is 9-11 and 5-6')
            speak('which time is good for you?')
        elif '9 to 11' in query:
            speak('your appointment has been booked for 9-11')
            response = sms.send(message, phone)
            print(response)
        elif '5 to 6' in query:
            speak('your appointment has been booked for 5-6')
            response = sms.send(message, phone)
            print(response)
        elif 'thank you' in query:
            speak('you are welcome')



