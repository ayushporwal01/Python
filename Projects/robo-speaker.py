import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

#welcome
print("Welcome To RoboSpeaker!")

while True:
    text = input("Enter what you want me speak: ")
    
    if text == "q":
        break
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()
