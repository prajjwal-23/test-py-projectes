import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') # to get voice id from our pc
engine.setProperty('voices', voices[1].id) # ==  1 for David 0 for Zira


def speech(audio):
    ''' this function takes input from the user and give output by speaker '''
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    ''' this fuction wish us acordind to the time '''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speech("good morning!")
    elif hour>=12 and hour<18:
        speech("good afternoon!")
    else:
        speech("good Evening!")
    
    print("Sir, I am Tony. Please tell me how may I help you")
    speech("Sir, I am Tony. Please tell me how may I help you")
    

def takeCommand():
    ''' this fuction take command from the microphone from the user '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please!")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speech('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences = 2 )
            speech('Accordindg to Wikipedia')
            print(results)
            speech(results)

        elif 'open youtube' in query:
            speech('opening sir')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speech('opening sir')
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            speech('opening sir')
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speech('playing sir')
            music_dir = "C:\\Users\\Prajjwal\\Desktop\\Toni the AI\\music"        
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speech(f"sir, the time is{strTime}")

        elif "your name" in query:
            speech("sir, my name is Tony. I am a AI, made by Prajjwal")

        elif "open vs code" in query:
            speech('opening sir')
            vs_location = "C:\\Users\\Prajjwal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_location)
        elif "open work box" in query:
            speech('opening sir')
            this_pc = "E:\\Workbox"
            os.startfile(this_pc)

        elif "quit" in query:
            speech('okay sir, byee')
            break