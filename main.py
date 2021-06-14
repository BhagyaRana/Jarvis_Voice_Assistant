# All Packages to Import

# pip install pyttsx3
# pip install SpeechRecognition
# pip install pipwin
# pipwin install pyaudio
# pip install pywhatkit
# pip install PyAutoGUI
# pip install wolframalpha
# pip install wikipedia
# pip install git+https://github.com/abenassi/Google-Search-API
# pip install playsound
# pip install speedtest-cli
# pip install psutil
# pip install pyjokes

# Python Test to Speech Package
import operator

import pyttsx3
# Package to Recognise the Speech
import speech_recognition as sr
# For Date and Time
import datetime
# For Opening the Applications
import os
# Open any Website
import webbrowser
# To Play Song on YouTube
import pywhatkit
# To Increase/Decrease the System Volume
import pyautogui
# For Opening any System Application [Calculator]
from subprocess import call
# For Searching Anything
import wolframalpha
# For Searching Something in Wikipedia
import wikipedia
# For Searching via Google API
import googleapi
from googleapi import google
# For Weather
import requests
import json
# For Internet Speed
import speedtest
# For Internet Availibility
import urllib.request
# For Memory Usage
import psutil
# For Jokes
import pyjokes
# For Delay
import time

# Voice Initialization Part for Jarvis

# Helps in synthesis and recognition of voice.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id) # [0 -> David, 1 -> Zira]
engine.setProperty('voices', voices[0].id)

# Function to Convert Text to Speech
def speak(text):
    engine.say(text)
    print("Command: " + text)
    engine.runAndWait()

# Function to Take Command [Voice] From User and Convert to text
def take_command():
    r = sr.Recognizer()
    # time.sleep(5)
    with sr.Microphone() as source:
        print("listening...[1 sec Delay]")
        # So Jarvis, Doesn't Leave the Command in Middle
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

# Function to Greet the User
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Sir")
    elif hour>12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am your Personal Assistant Jarvis, How can I Help You Sir?")

# Function to Check if Internet Connection is Available
def connect(host='https://www.google.com/'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

# Function to Read News
def News():
    # Change the API_KEY to your One

    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "YOUR_API_KEY_HERE"
    }
    main_url = " https://newsapi.org/v1/articles"
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    article = open_bbc_page["articles"]
    results = []
    for ar in article:
        results.append(ar["title"])
    for i in range(len(results)):
        print(i + 1, results[i])
        speak(results[i])

# Function for Calculations
# def get_operator(op):
#     return{
#         '+': operator.add(),
#         '-': operator.sub(),
#         'x': operator.mul(),
#         'divided': operator.__truediv__(),
#         'mod': operator.mod(),
#         }[op]

def evaluate(op1, operation, op2):
    op1 = int(op1)
    op2 = int(op2)
    if(operation == '+'):
        return op1+op2
    elif(operation == '-'):
        return op1-op2
    elif (operation == 'multiply'):
        return op1*op2
    elif (operation == "divide"):
        if(op2!=0):
            return op1/op2
        else:
            speak("Divide by Zero Error")
            return -1

    # return get_operator(operation)(op1, op2)

if __name__ == "__main__":
    greet()
    while True:

        query = take_command().lower()

        # All Task that Can be Performed by Jarvis

        # 1) Open any Application
        if "open notepad" in query:
            note_path = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(note_path)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif 'open code' in query:
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open youtube' in query:
            url = 'https://www.youtube.com/'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open_new(url)

        # 2) Play Any Random Music or Particular Music
        elif 'play' in query:
            song = query.replace('jarvis', '')
            song = song.replace('play', '')
            txt = "playing" + song
            speak(txt)
            pywhatkit.playonyt(song)

        # 3) Increase/decrease the speakers master volume
        elif 'volume up' in query:
            pyautogui.press("volumeup")
        elif 'volume down' in query:
            pyautogui.press("volumedown")
        elif 'volume mute' in query or 'mute' in query:
            pyautogui.press("volumemute")

        # 4) Opens any System App [For Eg: Calculator]
        elif 'open calculator' in query:
            call(["calc.exe"])

        # 5) Tells about something, by searching on the internet
        elif 'open google' in query:
            speak("Sir, What should I search on Google?")
            cm = take_command().lower()
            webbrowser.open_new(f"{cm}")

        elif 'who is' in query:
            name = query.replace('jarvis', '')
            name = name.replace('who is', '')
            info = wikipedia.summary(name)
            print(info)
            speak(info)

        elif 'wikipedia' in query:
            speak('searching wikipedia...')
            to_search = query.replace('jarvis', '')
            to_search = to_search.replace('wikipedia', '')
            results = wikipedia.summary(to_search, sentences=2)
            speak('According to Wikipedia, ')
            speak(results)

        #6) Tells the weather for a place
        elif 'weather' in query:
            # This is my API KEY, Change it to Yours
            api_key = "YOUR_WEATHER_API_KEY_HERE"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("Sir, For Which Place you want to know the Weather?")
            place = take_command().lower()
            complete_url = base_url + "appid=" + api_key + "&q=" + place
            response = requests.get(complete_url)
            x = response.json()
            if response.status_code == 200:
                y = x['main']
                current_temperature = y['temp']
                z = x['weather']
                weather_description = z[0]['description']
                # print following values
                t3 = "Temperature at " + place + " is " + str(current_temperature) + " Kelvin and Climate is " + str(weather_description)
                print(t3)
                speak(t3)
            else:
                speak("City Not Found Sir")

        #7) Tells the current time and/or date
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            t1 = "Current Time is " + time
            speak(t1)
        elif 'date' in query:
            from datetime import date
            today = date.today()
            d2 = today.strftime("%B %d, %Y")
            t2 = "Today is " + d2
            print(t2)
            speak(t2)

        #8) Set an Alarm
        elif 'alarm' in query:
            speak("Sir, Please tell me the time to set the alarm, Example - set alarm for 6:30 am")
            res = take_command().lower()
            res = res.replace('set alarm for', '')
            res = res.replace('.', '')
            res = res.upper()
            print(res)
            import MyAlarm
            MyAlarm.alarm(res)

        #9) Tell the Internet Speed
        elif 'internet speed' in query:
            st = speedtest.Speedtest()
            download_speed = str(round(float(st.download()/1000000)))
            upload_speed = str(round(float(st.upload()/1000000)))
            t5 = f"Sir, You Internet Connection has {download_speed} mega byte per seconds Downloading Speed and {upload_speed} mega byte per second Uploading Speed."
            print(t5)
            speak(t5)

        #10) Internet Connection
        elif 'internet connection' in query:
            if connect()==True:
                msg1 = "Internet Connection Available Sir"
                print(msg1)
                speak(msg1)
            else:
                msg2 = "Internet Connection Not Available Sir"
                print(msg2)
                speak(msg2)

        #11) Tell the Daily News
        elif 'news' in query:
            News()

        #12) Spell a Particular Word
        elif 'spell' in query:
            speak("Sir, Please tell me the word to Spell")
            res = take_command().lower()
            for i in res:
                speak(i)

        #13) How much Memory Consumed
        elif 'memory' in query:
            process = psutil.Process(os.getpid())
            msg3 = "Memory Consumed by your computer is " + str(process.memory_info()[0]/1000000) + " Mega bytes"
            print(msg3)
            speak(msg3)

        #14) Calculate
        elif 'calculate' in query:
            speak("What do you want to calculate? Example : 5 plus 10")
            res = take_command().lower()
            msg6 = evaluate(*(res.split(" ")))
            t7 = "Your Result is " + str(msg6)
            print(t7)
            speak(t7)

        # 15) help
        elif 'help' in query:
            speak('I can Help you to Open an Application Play Music, Search for Something, Tell you Time, Date, News, Internet Connection and Speed, Memory Consumptiom and much more.')

        #16) Jokes
        elif 'joke' in query or 'jokes' in query:
            msg9 = pyjokes.get_joke()
            print(msg9)
            speak(msg9)

        #17) Author
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Bhagya Rana.")

        # 18) exit
        elif 'exit' in query:
            speak("Thanks for giving me your precious time Sir")
            exit()