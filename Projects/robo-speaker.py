from pyttsx3 import speak

print("Welcome To RoboSpeaker!")

while True:
    speak("Enter what you want me to speak: ")
    text = input("Enter what you want me speak: ")

    if text == "q":
        speak("Thank You for using RoboSpeaker!")
        break

    speak(text)