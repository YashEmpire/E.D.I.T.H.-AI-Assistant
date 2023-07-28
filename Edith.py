import datetime
import time
import pyautogui
import requests
import speech_recognition as sr
import os
import pywhatkit as kit
import sys
import wikipedia
import webbrowser
import pyjokes
import smtplib
import pyttsx3
from requests import get

#To convert Text to Speech
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

#To wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        say("Good Morning")
    elif hour>12 and hour<18:
        say("Good Afternoon")
    else:
        say("Good Evening")

#To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language="en-in")
            list = query.split()

            for i in range(0, len(list)):

                if list[i].lower() == "edit":
                    list[i] = "Edith";

            query = " ".join(list)
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some ERROR Occurred. Sorry from Edith"

#To send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 535)
    server.ehlo()
    server.starttls()
    server.login('yashamre00@gmail,com', 'kmregpijvmxhkdxh')
    server.sendmail('yashamre00@gmail.com', to, content)
    server.close()

    def check_web_server(host, port, path):
        h = httplib.HTTPConnection(host, port)
        h.request('GET', path)
        resp = h.getresponse()
        print
        'HTTP Response:'
        print
        '   status =', resp.status
        print
        '   reason =', resp.reason
        print
        'HTTP Headers:'
        for hdr in resp.getheaders():
            print
            '  %s: %s' % hdr

#To get news and its update
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d033a5bf45d84917b13ec07a7649068d'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        print(f"Today's {day[i]} news is: {head[i]}")
        say(f"Today's {day[i]} news is: {head[i]}")


if __name__ == '__main__':
    print("PyCharm")
    wish()
    say("Hello I am Edith AI")
    while True:
        print("Listening...")
        query = takecommand()
        sites = [["youtube", "https://www.youtube.com"], ["facebook", "https://www.facebook.com/"], ["google", "https://www.google.com"], ["wikipedia", "https://www.wikipedia.com"], ["cricbuzz", "https://www.cricbuzz.com/"], ["Linkedin", "https://www.linkedin.com/in/yash-amre-0b84a6242/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir...")
                say("Sir what u wanna search for")
                print("Listening..")
                cm = takecommand().lower()
                webbrowser.open(site[1]+"/search?q="+cm)

        if "open music" in query:
            musicPath = "C:/Users\HP\Downloads\Bella_Ciao.mp3"
            os.system(f"start {musicPath}")

        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            sec = datetime.datetime.now().strftime("%S")
            say(f"Sir the time is {hour} {min} {sec}")

        if "open discord" in query:
            discordpath = "C:/Users\HP\OneDrive\Desktop\Discord"
            os.system(f"start {discordpath}")

        if "open Notepad" in query:
            notepadpath = "C:/Users\HP\Downloads/Notepad"
            os.system(f"start {notepadpath}")

        if "open command prompt" in query:
            os.system("start cmd")

        if "IP address" in query:
            ip = get("https://api.ipify.org").text
            print(ip)
            say(f"Your ip address is {ip}")

        if "Wikipedia" in query:
            print("Searhing Wikipedia...")
            say("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            say("According to wikipedia....")
            print(results)
            say(results)

        if "send message" in query:
            kit.sendwhatmsg("+918767406824", "Virat Kohli", 1,25)

        if "play songs on YouTube" in query:
            kit.playonyt("Jai Shri Ram")

        if "email to Yash" in query:
            try:
                say("What Should I say?")
                print("Listening...")
                content= takecommand().lower()
                to = "yashamre2@gmail.com"
                sendEmail(to, content)
                say("Email has been sent to Yash")

            except Exception as e:
                print(e)
                say("Sorry sir, i am not able to sent this email to Yash")

        if "no thanks" in query:
            say("Dhanyawad, aajun kahi asel tar, aamhala nakkich kalva")
            sys.exit()

        if "close notepad" in query:
            say("Okay Sir, closing Notepad")
            os.system("taskkill /f /im Notepad.exe")

        if "close Pokemon" in query:
            say("Okay Sir, closing Discord")
            os.system("taskkill /f /im discord.exe")

        if "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            say("Alarm has been set")
            if nn == 2:
                music_dir = "C:/Users\HP\Downloads"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        if "tell me a joke" in query:
            jokes = pyjokes.get_joke()
            print(jokes)
            say(jokes)

        if "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        if "tell me the news" in query:
            say("Please wait sir, fetching the latest news")
            news()
            print(news())

        if "shut down the system" in query:
            os.system("shutdown /s /t 5")

        if "restart the system" in query:
            os.system("shutdown /r /t 5")

        if "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


        say(query)