import speech_recognition as sr
import subprocess

recognizer = sr.Recognizer()

with sr.Microphone as source:
    print("Say the app name...")
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio).lower()
    print("You said: ", command) 

    if "chrome" in command:
        subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe"])
    elif "notepad" in command:
        subprocess.Popen(["notepad.exe"])
    elif "gmail" in command:
        subprocess.Popen(["gmail.exe"])
    elif "file-explorer" in command:
        subprocess.Popen(["file-explorer"])
    else:
        print("Can't open this app")

except Exception as e:
    print("Error: ", e)
        