import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import re
import time
import smtplib
from pathlib import Path

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')            #getting details of current voice
engine.setProperty('voice', voices[1].id)
'''
############################################################################################################
############################################################################################################
                                    Don't Edit The Part Above This Section                                      
############################################################################################################
############################################################################################################
'''
def change_prop0():
    engine.setProperty('voice', voices[1].id)
def change_prop1():
    engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio) 
    engine.runAndWait()         #Without this command, speech will not be audible to us.
def wishMe():
    speak("Initializing system.")
    speak(" Starting JARVIS. Please WAIT.")
    time.sleep(2)
    speak("JARVIS Online")
    time.sleep(1)
    change_prop1()
    hour = int(datetime.datetime.now().hour)
    if hour>=8 and hour<12:
        speak("Good Morning, Sir")
    elif hour>=12 and hour<14:
        speak("Good Afternoon, Sir")
    elif hour>=14 and hour<18:
        speak("Good Evening, Sir")
    else:
        speak("Have a great night, Sir")
    speak("I am your Personal assistant JARVIS. How may I help you.")
def sendEmail(to, content,mail_id,psword):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(f'{mail_id}', f'{psword}')
    server.sendmail(f'{mail_id}', to, content)
    server.close(    )
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')     #Using google for voice recognition.
        print(f"User said: {query}\n")                          #User query will be printed.
    except Exception as e:
        print(e)    
        print("Please Repeat Clearly")   #Say that again will be printed in case of improper voice/input in another language 
        speak("Please Repeat Clearly")   
        return "None"                       #None string will be returned
    return query
def template():
    print("\n\n                            Welcome to JARVIS Interface.          \n")
    print("             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!          \n")
    print("                                   COMMAND CENTER \n")
    print("         Please Use The Following Commands To Executing The Required Task  \n")
    print("\t  [1] Open Youtube                - To Open www.youtube.com\n")
    print("\t  [2] Open Google                 - To Open www.google.com\n")
    print("\t  [3] Open Github                 - To Open www.github.com\n")
    print("\t  [4] Open VsCode Application/App - To Open the VsCode app\n")
    print("\t  [5] Open Chrome Browser         - To Open the Chrome Browser\n")
    print("\t  [6] Tell me the time            - To know the exact time according to your time zome\n")
    print("\t  [7] Send an E-mail              - To send an E-mail \n")
    print("\t  [8] Exit Jarvis                 - To stop the programme for Jarvis\n")


if __name__ == "__main__":
    wishMe()
    template()
    a=True
    while a:
        query = takeCommand()
        query=query.lower()   #Converting user query into lower case
        # Logic for executing tasks based on query
        if 'wikipedia' in query:        #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia!')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4) 
            speak("According to Wikipedia")
            print(f"Wikipedia: {results}")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")       
        elif 'open github' in query:
            webbrowser.open("https://github.com/")       
        elif 'open vs code' in query:
            codePath = "C:\\Users\\hrish\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code"
            os.startfile(codePath)
        elif ('open'  in query) and ('chrome' in query ) :
            chromePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get('chrome').open("google.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif ('send'  in query) and ('email' in query ):
            regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
            try:
                c=True
                speak("Please enter your Email Id")
                mail_id=input("Please enter your Email Id:  ")
                speak("Please enter your Password:")
                psword=input("Please enter your Password:  ")
                while(a):
                    c=False
                    speak("Sir, now please enter the Email Id of the reciever")
                    to=input("Please enter the Email Id of the reciever:\t")
                    c2=True
                    while(c2):
                        if(re.search(regex,mail_id)):
                            speak("What should I send, Sir?")
                            content = takeCommand()
                            sendEmail(to, content,mail_id,psword)
                            speak("Email has been sent!")
                            c2=False
                        else:
                            speak("Sir, Please enter a valid Email Id")
                
                speak("What should I send, Sir?")
                content = takeCommand()
                sendEmail(to, content,mail_id,psword)
                speak("Email has been sent!")
                
            except Exception as e:
                print(e)
                speak("Sorry Sir. I was not able to send this email")    
                speak("I regret the inconvenience. Please try again!") 
        elif 'exit' in query:
            a=False
            speak("Closing High Security Database,. Imposing Lockdown. JARVIS, Shutting down, in:")
            speak("3,")
            speak("2,")
            speak("1,")
            change_prop0()
            speak("All systems closed. Have a nice Day Sir")


 