import speech_recognition as sr  
import webbrowser as wb
import pyttsx3
import subprocess
import time

def music():
    with sr.Microphone() as source:
        audio = r.listen(source)  

        try:
            text =  r.recognize_google(audio)
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say('You said '+text)
            engine.runAndWait()
            print('You Said: '+text)
            wb.open('https://wynk.in/music/detailsearch/'+text+'?q='+text)
        except sr.UnknownValueError:
            print("Could not understand audio")
def search():
    with sr.Microphone() as source:
        audio = r.listen(source)  

        try:
            text =  r.recognize_google(audio)
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say('You said '+text)
            engine.runAndWait()
            print('You Said: '+text)
            a=text.split()
            wb.open('https://www.google.com/search?client=firefox-b-d&q='+text)
        except sr.UnknownValueError:
            print("Could not understand audio")
def app():
     with sr.Microphone() as source:
        audio = r.listen(source)  

        try:
            text =  r.recognize_google(audio)
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say('You said '+text)
            engine.runAndWait()
            print('You Said: '+text)
            if text== 'steam':
                subprocess.call('C:/Program Files (x86)/Steam/Steam.exe')
            elif text=='NetBeans':
                subprocess.call('C:/Users/Rijin Thomas/Downloads/netbeans-11.1-bin/netbeans/bin/netbeans64.exe')
            elif text=='YouTube':
                wb.open('https://www.youtube.com/')
            elif text=='VLC':
                subprocess.call("C:/Program Files (x86)/VideoLAN/VLC/vlc.exe")
            else:
                print("Sorry! App not found!, Please try again")
        except sr.UnknownValueError:
            print("Could not understand audio")
r = sr.Recognizer()
while(1):
    #print("Speak any of the following to perform an action\n1.play music\n2.search on Google\n3.open app")
    with sr.Microphone() as source:                                                                                                                                                        
        audio = r.listen(source)  
        try:
            text1 =  r.recognize_google(audio)
            print(text1)
            if text1=='hi Friday':
                engine = pyttsx3.init()
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[1].id)
                engine.say('Hey, what can i do for you')
                time.sleep(2)
                print('Try Saying....\n Play Music \n Search on Google \n Open App\n')
                engine.runAndWait()
                with sr.Microphone() as source:                                                                                                                                                        
                    audio = r.listen(source)
                    try:
                        text =  r.recognize_google(audio)
                        print('Done!')
                        print(text)
                        if(text=="play music"):
                            print('What song would you like to play')
                            music()
                        elif text=="search on Google":
                            print("What would you like to search")
                            search()
                        elif text=='open app':
                            print("Which app would you like to open?")
                            print('1.Steam \n 2.VLC \n 3.Netbeans \n 4.Youtube')
                            app()
                        elif(text=="that's all"):
                            exit()
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                    except sr.RequestError as e:
                        print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
                    print("Could not understand audio")