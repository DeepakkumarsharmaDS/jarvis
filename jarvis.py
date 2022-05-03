import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

def takeCommand():
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
        speak("Say that again please...")
        print("Say that again please...") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening youtube sir")
            webbrowser.open("google.com")

        elif 'open stack over flow' in query:
            speak("opening stack over flow sir")
            webbrowser.open("stackoverflow.com")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'email to goku' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "gokeEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend goku  bhai. I am not able to send this email")

        elif 'hi jarvis' in query or 'hello jarvis' in query:
            speak("Hello sir...!!! How are you?")

        elif 'good' in query or 'i am fine' in query:
            speak("that's great sir, happy to hear that")

        elif 'how are you' in query:
            speak("i am fine sir, let me know if you need some help.")

        elif 'ok' in query:
            speak("okay")

        elif 'who are you' in query:
            speak("i am a virtual assistant. Can do certain things")

        elif 'quit' in query or 'exit' in query or 'quit jarvis' in query or 'exit jarvis' in query or 'bye' in query or 'bye jarvis' in query:
            speak("Thank you Sir for your time .  !!!! Have a nice day. ...")
            break
        elif 'open chrome' in query:
            speak("opening chrome")
            os.system("google chrome")

        elif 'close chrome' in query:
            speak("closing chrome sir")
            os.system("taskkill /f /im chrome.exe")

        elif 'play excuse song' in query:
            speak("playing that song for you sir..")
            webbrowser.open("https://youtu.be/vX2cDW8LUWk")

        elif 'open notepad' in query:
            speak('Opening Notepad')
            os.system("start notepad")

        elif 'close notepad' in query:
            speak("Closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'open wordpad' in query:
            speak("Opening Wordpad")
            os.system("start wordpad")

        elif 'close wordpad' in query:
            speak("Closing Wordpad")
            os.system("taskkill /f /im wordpad.exe")

        elif 'open whatsapp' in query:
            speak("opening whats app sir")
            webbrowser.open("whats web.com")  

        elif 'close whatsapp' in query:
            speak("closing whats app")
            os.system("taskkill /f /im whatsweb.com")

        elif 'open camera' in query:
            speak("opening camera sir..!take a nice pic sir.")
            os.system("start microsoft.windows.camera:")

        elif 'close camera' in query:
            speak("closing camera sir")
            os.system("taskkill /f /im windowscamera.exe")

        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")

        elif 'close spotify' in query:
            speak("closing spotify")
            os.system("taskkill /f /im spotify.com")

        elif 'who is salman khan' in query:
            speak("salmaan khan is a heavy driver sir. hehe")

        elif 'open calculator' in query:
            speak("opening calculator")
            os.system("start calc")

        elif 'open control panel' in query:
            speak("opening control panel")
            os.system("start control panel")

        elif 'open' in query:
            speak("what should i open sir....")

        elif 'jarvis' in query:
            speak("Anything for me, sir!")

        elif 'what are you doing jarvis' in query:
            speak("i am learning something new!")

        elif 'open facebook' in query:
            speak(" opening facebook sir")
            