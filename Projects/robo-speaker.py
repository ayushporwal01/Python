from pyttsx3 import speak

print("Welcome To RoboSpeaker!")

while True:
    text = input("Enter what you want me speak: ")

    if text == "q":
        print("Thank You for using RoboSpeaker!")
        break

    speak(text)