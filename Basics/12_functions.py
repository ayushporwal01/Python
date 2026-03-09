#A function is a reusable block of code used to perform specific task.

def greetHello(name):
    print("Hello " + name)

def letterGenerator(name, date):
    st = f"Hi, this is {name} and i would like to invite you to my birthday on {date}."
    print(st)

greetHello("Ayush") 
letterGenerator("Ayush", "December 27th, 2026")