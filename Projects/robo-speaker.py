import pyttsx3

#welcome
print("Welcome To RoboSpeaker!")

while True:
    text = input("Enter what you want me speak: ")
    
    if text == "q":
        print("Goodbye!")
        break
    
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
