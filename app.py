# -*- coding: utf-8 -*-

import pyttsx3
import speech_recognition as sr
import subprocess
import tkinter as tk
from tkinter import messagebox
import json
import random
import operator
import datetime
import webbrowser
import os
import smtplib
import time
import requests
import win32com.client as wincl
from urllib.request import urlopen
import shutil
import pyaudio
import africastalking

# Initialize africastalking
africastalking.initialize(
    username='Kwepo',
    api_key='f67c169248ae4bf36bdc9e798afed8428dcd3770bf78cf051d4faa752fd8a8a9',
)
sms = africastalking.SMS
message = "Thank you for booking an Appointment with us."
phone = "+254714805460"

# Initialize pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to make the assistant speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to wish the user based on the time of day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon ")
    else:
        speak("Good Evening")

    assname = "Wanjiku"
    speak("I am your Assistant")
    speak(assname)
    speak("How can I help you")

# Function to take voice commands from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 0.5
        print("Listening...")
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to recognize your voice.")
        speak("Unable to recognize your voice.")
        return "None"
    return query

# Function to handle user commands
def handleCommand():
    query = takeCommand().lower()
    if 'hello' in query:
        speak('Hello, I am Jane your booking assistant')
        speak('How may I help you?')
    elif 'book an appointment' in query:
        speak('Which department?')
    elif 'optical' in query:
        speak('Okay..')
        speak('What is your name')
        uname = takeCommand()
        speak('Welcome to Blue Hospital')
        speak(uname)
        speak('Time available is 9-11 and 5-6')
        speak('Which time is good for you?')
    elif '9 to 11' in query:
        speak('Your appointment has been booked for 9-11')
        response = sms.send(message, [phone])
        print(response)
    elif '5 to 6' in query:
        speak('Your appointment has been booked for 5-6')
        response = sms.send(message, [phone])
        print(response)
    elif 'thank you' in query:
        speak('You are welcome')

# Function to initialize the UI
def initUI():
    root = tk.Tk()
    root.title("Virtual Assistant")

    canvas = tk.Canvas(root, height=500, width=800)
    canvas.pack()

    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    button = tk.Button(frame, text="Speak", font=40, command=handleCommand)
    button.place(relx=0.7, relheight=1, relwidth=0.3)

    label = tk.Label(frame, text="Click 'Speak' and say your command", font=40)
    label.place(relx=0, relheight=1, relwidth=0.65)

    lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    text_box = tk.Text(lower_frame, font=40)
    text_box.place(relx=0, rely=0, relwidth=1, relheight=1)

    scrollbar = tk.Scrollbar(text_box)
    scrollbar.pack(side='right', fill='y')
    text_box.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_box.yview)

    root.mainloop()

if __name__ == '__main__':
    wishMe()
    initUI()
