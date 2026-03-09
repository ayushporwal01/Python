import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

#welcome
print("Welcome To RoboSpeaker!")

while True:
    text = input("Enter what you want me speak: ")
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()
