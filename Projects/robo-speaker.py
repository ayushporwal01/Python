from pyttsx3 import speak

# welcome
print("Welcome To RoboSpeaker!")

while True:
    text = input("Enter what you want me speak: ")

    if text == "q":
        print("Goodbye!")
        break

    speak(text)