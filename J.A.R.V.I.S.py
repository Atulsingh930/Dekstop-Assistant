
import os
import smtplib
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
from AppOpener import run
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis, How can i help you")

def takeCommand():
    '''It takes microphone input from the user and return string output'''
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in" )
        print(f"user said: {query}\n")
    except Exception as e:
        print("say that again please....")
        return "None"
    return query
def sendemail(to, content):
    server = smtplib.SMTP("smatp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "yo ur-password")
    server.sendmail("youremail@gmail.com", to, content)
    server.close()
if __name__ =="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2) 
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open calxypod" in query:
            webbrowser.open("calxypod.com")
        
        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is, {strtime}")
            print(f"The time is, {strtime}")
        elif "open code" in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 
        elif "email to Atul" in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "youremail@gmail.com"
                sendemail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able send this email")
        elif "spotify" in query:
            speak("wait for moment")
            run("spotify")
        elif "bye bye" in query:
            speak("chalo main chalti ho")
            quit()