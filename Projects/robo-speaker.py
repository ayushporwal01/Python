import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Text to speak
text = input("Enter what you want me speak: ")

# Speak the text
engine.say(text)
engine.runAndWait()
