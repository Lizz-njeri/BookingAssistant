from gtts import gTTS
import os
import speech_recognition as sr
import datetime

def speak(audio):
    tts = gTTS(text=audio, lang='en')
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")  # You might need to install mpg321 to play the audio

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    ass_name = "Jane"
    speak("I am your Assistant")
    speak(ass_name)
    speak("How can I help you")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
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

if __name__ == '__main__':
    clear = lambda: os.system('clear')  # Use 'clear' instead of 'cls' for Linux
    clear()
    wish_me()

    while True:
        query = take_command().lower()

        if 'hello' in query:
            speak('Hello, I am Jane, your booking assistant.')
            speak('How may I help you?')
        elif 'i want to book an appointment' in query:
            speak('Which department?')
        elif 'optical' in query:
            speak('Okay...')
            speak('What is your name?')
            user_name = take_command()
            speak('Welcome to Blue Hospital')
            speak(user_name)
            speak('Available appointment times are from 9 to 11 and 5 to 6. Which time is good for you?')
        elif '9 to 11' in query:
            speak('Your appointment has been booked for 9 to 11')
        elif '5 to 6' in query:
            speak('Your appointment has been booked for 5 to 6')
