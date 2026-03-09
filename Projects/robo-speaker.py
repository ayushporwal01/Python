import subprocess

print("Welcome To RoboSpeaker!")

x = input("Enter what you want me to speak: ")

command = f"say {x}"
subprocess.run(command)