from pyttsx3 import speak

print("Welcome To RoboSpeaker!")

while True:
    text = input("Enter what you want me speak: ")

    if text == "q":
        speak("Thank You for using RoboSpeaker!")
        break

    speak(text)