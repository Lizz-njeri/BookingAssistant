import pyttsx3
import speech_recognition as sr
import datetime
import africastalking

# Initialize Africa's Talking API with your credentials
username = "valeria"
api_key = "9e83ab8823796fee6abee2b9477314a71da6ae063fc6ec4f9d04132da0193888"
africastalking.initialize(username, api_key)

# Create an SMS service
sms = africastalking.SMS

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    assname = "Jane"
    speak(f"I am your Assistant, {assname}")
    speak("How can I help you today?")

def sendSMS(phone_number, message):
    try:
        # Send the SMS
        response = sms.send(message, [phone_number])
        if response['SMSMessageData']['Recipients'][0]['status'] == 'Success':
            return True
        else:
            return False
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return False

if __name__ == '__main__':
    wishMe()

    while True:
        query = input("You: ").lower()

        if 'hello' in query:
            speak('Hello, I am Jane, your booking assistant.')
            speak('How may I help you?')

        elif 'i want to book an appointment' in query:
            speak('Which department would you like to book an appointment with?')

        elif 'optical' in query:
            speak('Okay...')
            speak('What is your name?')
            uname = input("You: ")

            speak('Welcome to Blue Hospital, ' + uname)
            speak('Appointment times available are 9-11 AM and 5-6 PM')
            speak('Which time slot would you prefer?')

        elif '9 to 11' in query:
            speak('Your appointment has been booked for 9-11 AM.')

            # Send an SMS notification
            phone_number = '+254714805460'
            sms_message = 'Your appointment at Blue Hospital has beenbooked for 9-11 AM.'
            if sendSMS(phone_number, sms_message):
                speak('An SMS notification has been sent to your phone.')
            else:
                speak('Failed to send SMS notification.')

        elif '5 to 6' in query:
            speak('Your appointment has been booked for 5-6 PM.')

            # Send an SMS notification
            phone_number = 'RECIPIENT_PHONE_NUMBER'
            sms_message = 'Your appointment at Blue Hospital has been booked for 5-6 PM.'
            if sendSMS(phone_number, sms_message):
                speak('An SMS notification has been sent to your phone.')
            else:
                speak('Failed to send SMS notification.')