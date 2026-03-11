import sounddevice as sd
import numpy as np
import speech_recognition as sr
import subprocess

# Settings
samplerate = 44100  # Sample rate
duration = 5        # Seconds to listen

print("Listening...")

# Record audio using sounddevice
audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
sd.wait()  # Wait until recording is finished

# Convert to AudioData for speech_recognition
recognizer = sr.Recognizer()
audio_bytes = sr.AudioData(audio_data.tobytes(), samplerate, 2)  # 2 bytes per sample

try:
    command = recognizer.recognize_google(audio_bytes).lower()
    print("You said:", command)

    # Launch apps based on command
    if "chrome" in command:
        subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe"])
    elif "notepad" in command:
        subprocess.Popen(["notepad.exe"])
    elif "gmail" in command:
        subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe", "https://mail.google.com"])
    elif "file explorer" in command:
        subprocess.Popen(["explorer.exe"])
    else:
        print("App not recognized")

except Exception as e:
    print("Error:", e)