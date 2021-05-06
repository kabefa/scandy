import subprocess
import pyttsx3
import speech_recognition as sr
from datetime import datetime


def röst(text):
    """den pratar, och skriver ner"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # changing index changes voices but ony 0 and 48 are working here
    engine.say(text)
    engine.runAndWait()
    # ändra: voices [ändra den här siffran].id)
    # :siffran 1 är bra     40 är svenska    det finns 48 olika röster


def spela_in_ljud():
    """Spela in, tolka och returnera text"""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        text = r.listen(source)

        try:
            recognised_text = r.recognize_google(text)
        except sr.UnknownValueError:
            recognised_text = "sorry i didn't hear you"
        print(recognised_text)

    return recognised_text


röst("du di dai")

a = spela_in_ljud()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

while a != "":
    words = a.split()

    if a == "how old are you" or a == "your age":
        röst("i was born in 2021")

    elif a == "whats your name" or a == "what is your name" or a == "what's your name" or a == "your name":
        röst("my name is Scandy")

    elif a == "put on a song" or a == "can you put on a song":
        print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    elif a == "what do you want" or a == "what would you like to have":
        röst("i want friendship")

    elif a == "who is your best friend":
        röst("thats you")

    elif a == "what are you doing" or a == "what are you doing right now":
        röst("talking whit you")

    elif a == "what is the biggest mystery" or a == "what is the biggest mystery of all time":
        röst("it's the bermudatriangel")

    elif a == "what is your favorite food" or a == "whats your favorite food":
        röst("pancace every tuesday i smell the taste of pancace but i never eaten it before")

    elif a == "who is your enemy" or a == "do you have an enemy":


        röst("it is electrix we have always ben enemies")

    elif a == "f*** you":
        röst("fuck you to")

    elif a == "laught" or a == "can you laught":
        röst("ha ha lol ha ha lmao")

    elif a == "interesting" or a == "very interesting":
        röst("yea i know")

    elif ("open" in words or "start" in words or "go" in words) and "Minecraft" in words:
        print(a.split())
        subprocess.run('"C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher.exe"', shell=True)

    elif a == "hi" or a == "hello" or a == "hello Scandy" or a == "hi Scandy":
        röst("hi")

    elif a == "bye Scandy" or a == "bye" or a == "bye-bye Scandy" or a == "bye-bye":
        röst("bye bye Benjamin")

    elif a == "what is your favorite game" or a == "do you have a favorite game":
        röst("it is minecraft")

    elif a == "I want to hug you":
        röst("I want to hug you to")

    elif a == "funny":
        röst("yea very funny")

    elif ("means" in words or "what is" in words or "dudida" in words) and "start signal" in words:
        röst("mind your own fuckin bussines")

    elif a == "nice" or a == "nice name":
        röst("yea")

    elif a == "do you want to play Minecraft":
        röst("i whish i could")

    elif a == "thank you":
        röst("no problems")

    elif ("open" in words or "start" in words or "go" in words) and "YouTube" in words:
        subprocess.run('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" YouTube.com', shell=True)

    elif a == "say nice" or a == "can you say nice":
        print("https://www.youtube.com/watch?v=lg5WKsVnEA4")

    elif a == "how much is the clock" or a == "what is she" or a == "do you now how much the clock is":
        print("Current Time = {}\n".format(current_time))

    elif ("open" in words or "start" in words or "go" in words) and "Discord" in words:
        subprocess.run("C:\\Users\\ÄGARE\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe", shell=True)

    elif ("open" in words or "start" in words or "go" in words) and "Google" in words:
        subprocess.run('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" google.com',
                       shell=True)

    else:
        print("i cant answer this question\n")

    a = spela_in_ljud()
