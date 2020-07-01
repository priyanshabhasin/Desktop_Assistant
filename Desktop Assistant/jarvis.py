import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Mam!! Please tell me how may I help you")

def takeCommand():
    #it takes microphone input from the user and return string as output    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        # speak(audio)
        
    
    try:
        
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')         
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        print("Say that again please...")   
        return "None" 
    return query

if __name__ == "__main__":
    wishMe()
    
    while True:
        query=takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace('wikipedia', "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H hours%M minutes and%S seconds")
            speak(f"the time is:{strTime}")

        elif 'open code' in query:
            codePath="C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'what is your name' in query:
            speak("My name is jarvis!how can I help u mam")
        elif 'how are you' in query:
            speak("I am good...what about you")
        elif 'you are a very good assistant' in query:
            speak("Thank you")
        elif 'bye jarvis' in query:
            speak('Bye!have a nice day')