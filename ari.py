import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import threading
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    '''
    Greeting Function to be called when User runs the program
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak("Good morning Vansh!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Vansh!")
    else :
        speak("Good Evening Vansh")

    speak("I am aari, Your virtual assistant, How may I help you today?")
    print("How can I help you Sir?")

def takeCommand():
    '''
    Taking Command from Vansh and returning string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = r.listen(source, timeout=5)  # Listen for audio input with a timeout of 5 seconds
        except sr.WaitTimeoutError:
            print("Timeout occurred while waiting for audio input.")
            return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Recognized: {query}\n")
        return query
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"


def close_ari(query):
    if 'bye' in query or 'stop' in query or 'close' in query or 'no' in query:
        speak('Have a nice day Vansh, Good bye')
        print("Byee")
        return True
    return False

def wikipedia_search(query):
    if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
    
def open_sites(query):
    if 'youtube' in query:
        speak("Opening Youtube..")
        webbrowser.open("youtube.com")
    elif 'google' in query:
        speak("Opening Google..")
        webbrowser.open("google.com")
    elif 'search'  in query:
        speak('Searching it on Google')
        webbrowser.open(f"https://www.google.com/search?q={query}")

def open_code(query):
    if 'code' in query:
        codepath = "C:\\Users\\Vansh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("opening visual studio code")
        os.startfile(codepath)

if __name__ == "__main__":
    greetings()
    run_once = True
    while run_once:
        query = takeCommand().lower()

        if query is None:
            continue

        if wikipedia_search(query):
            wikipedia_search(query)
            continue

        elif open_sites(query):
            open_sites(query)
            continue
        
        run_once = False
    
    print("Anything else sir?")
    speak('Anything else sir?')
    while True:
        query = takeCommand().lower()
        if close_ari(query):
            run_once = False
            break