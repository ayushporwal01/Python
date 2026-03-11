import speech_recognition as sr
import subprocess

recognizer = sr.Recognizer()

with sr.Microphone as source:
    print("Say the app name: ")
    audio = recognizer.listen(source)

try:
    