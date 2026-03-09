#A function is a reusable block of code used to perform specific task.
#fstrings lets us use variables inside strings.

def greetHello(name):
    print("Hello " + name)

def letterGenerator(name, date):
    st = f"Hi, this is {name}. \nI would like to invite you to my birthday on {date}."
    print(st)

def average(a, b):
    return (a + b)/2

greetHello("Ayush") 
letterGenerator("Ayush", "December 27, 2026")
print(average(56, 69))  #62.5