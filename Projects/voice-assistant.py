import speech_recognition as sr
import subprocess

recognizer = sr.Recognizer()

# Use SoundDevice instead of PyAudio
with sr.Microphone() as source:
    print("Say the app name...")
    recognizer.adjust_for_ambient_noise(source)  # optional, helps with background noise
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio).lower()
    print("You said:", command)

    if "chrome" in command:
        subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"])
    elif "notepad" in command:
        subprocess.Popen(["notepad.exe"])
    elif "calculator" in command:
        subprocess.Popen(["calc.exe"])
    else:
        print("App not recognized")

except Exception as e:
    print("Error:", e)