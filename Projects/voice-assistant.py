import speech_recognition as sr
import subprocess

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say the app name...")
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio).lower()
    print("You said: ", command) 

    if "open chrome" in command:
        subprocess.Popen(["rC:\Program Files\Google\Chrome\Application\chrome.exe"])
    elif "open notepad" in command:
        subprocess.Popen(["notepad.exe"])
    elif "open gmail" in command:
        subprocess.Popen(["rC:\Program Files\Google\Chrome\Application\chrome.exe" , "https://mail.google.com"])
    elif "open file-explorer" in command:
        subprocess.Popen(["explorer.exe"])
    else:
        print("Can't open this app")

except Exception as e:
    print("Error: ", e)
        