import speech_recognition as sr
import sounddevice as sd
import numpy as np
import subprocess

recognizer = sr.Recognizer()
fs = 44100  # sample rate
duration = 5  # recording duration in seconds

while True:
    print("Say the app name...")
    # Record audio using sounddevice
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished

    # Convert numpy array to AudioData for speech_recognition
    audio_bytes = sr.AudioData(audio_data.tobytes(), fs, 2)  # 2 bytes per sample

    try:
        command = recognizer.recognize_google(audio_bytes).lower()
        print("You said:", command)

        if "chrome" in command:
            subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe"])
            break
        elif "notepad" in command:
            subprocess.Popen(["notepad"])
            break
        elif "calculator" in command:
            subprocess.Popen(["calc"])
            break
        elif "youtube" in command:
            subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe", "https://youtube.com"])
            break
        elif "gmail" in command:
            subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe", "https://mail.google.com"])
            break
        elif "listenfree" in command:
            subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe", "https://listenfree.in""])
            break
        else:
            print("App not recognized. Try again.")

    except sr.UnknownValueError:
        print("Could not understand. Try again.")
    except sr.RequestError:
        print("Recognition service unavailable. Check your internet.")