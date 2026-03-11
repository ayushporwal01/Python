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

apps = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad",
    "calculator": "calc"
}

process_names = {
    "chrome": "chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "Calculator.exe"
}

websites = {
    "youtube": "https://youtube.com",
    "gmail": "https://mail.google.com",
    "listenfree": "https://listenfree.in"
}

while True:
    print("Say the app name to open or close...")
    
    # Record audio
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    audio_bytes = sr.AudioData(audio_data.tobytes(), fs, 2)

    try:
        command = recognizer.recognize_google(audio_bytes).lower()
        print("You said:", command)

        handled = False  # flag to prevent multiple actions

        # CLOSE apps first
        for app, proc_name in process_names.items():
            if f"close {app}" in command:
                for proc in psutil.process_iter(['pid', 'name']):
                    if proc.info['name'] == proc_name:
                        os.kill(proc.info['pid'], signal.SIGTERM)
                        print(f"{app} closed.")
                        handled = True
                break  # prevent multiple matches

        # OPEN apps
        if not handled:
            for app, path in apps.items():
                if f"open {app}" in command:
                    subprocess.Popen([path])
                    print(f"{app} opened.")
                    handled = True
                    break

        # OPEN websites
        if not handled:
            for site, url in websites.items():
                if site in command:
                    subprocess.Popen([apps["chrome"], url])
                    print(f"{site} opened.")
                    handled = True
                    break

        if not handled:
            print("Command not recognized. Try again.")

    except sr.UnknownValueError:
        print("Could not understand. Try again.")
    except sr.RequestError:
        print("Recognition service unavailable. Check your internet.")