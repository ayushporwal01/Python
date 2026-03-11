import speech_recognition as sr
import sounddevice as sd
import numpy as np
import subprocess
import os
import signal
import psutil  # pip install psutil

recognizer = sr.Recognizer()
fs = 44100  # sample rate
duration = 5  # recording duration in seconds

# Map app names to their launch paths or commands
apps = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad",
    "calculator": "calc"
}

# Map app names to process names for closing
process_names = {
    "chrome": "chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "Calculator.exe"
}

while True:
    print("Say the app name to open or close...")
    
    # Record audio
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    # Convert to AudioData
    audio_bytes = sr.AudioData(audio_data.tobytes(), fs, 2)

    try:
        command = recognizer.recognize_google(audio_bytes).lower()
        print("You said:", command)

        # OPEN apps
        for app in apps:
            if f"open {app}" in command:
                subprocess.Popen([apps[app]])
                print(f"{app} opened.")
                break

        # CLOSE apps
        for app in process_names:
            if f"close {app}" in command:
                for proc in psutil.process_iter(['pid', 'name']):
                    if proc.info['name'] == process_names[app]:
                        os.kill(proc.info['pid'], signal.SIGTERM)
                        print(f"{app} closed.")
                break

        # OPEN websites
        if "youtube" in command:
            subprocess.Popen([apps["chrome"], "https://youtube.com"])
        elif "gmail" in command:
            subprocess.Popen([apps["chrome"], "https://mail.google.com"])
        elif "listenfree" in command:
            subprocess.Popen([apps["chrome"], "https://listenfree.in"])

    except sr.UnknownValueError:
        print("Could not understand. Try again.")
    except sr.RequestError:
        print("Recognition service unavailable. Check your internet.")