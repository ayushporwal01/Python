#A string is a sequence of characters used to represent text.
#string is immutable

name = 'Ayush'
name2 = 'Ayushsh'
number = "7"

print(name)

print(name[0:3]) #Ayu
print(name.upper()) #AYUSH
print(name.capitalize()) #first character capitalized and rest converted to lowercase
print(name.count("A")) #1
print(name.endswith("h")) #True
print(name.find("h")) #4
print(name.center(15, "*")) #*****Ayush*****
print(name.isalnum()) #True
print(number.isalpha()) #False
print(number.isnumeric()) #True
print(number.isdigit()) #True
print(name.join(["", number])) #Ayush7
print(name.removeprefix("Ayu")) #sh
print(name.removesuffix("sh")) #Ayu
print(name.replace("s", "")) #Ayuh
print(name.replace("s", "")) #Ayuh
print(name2.strip("sh")) #Ayu

#valid string
a = "Ayush"
a = 'Ayush'
a = '''Ayush
Porwal''' #''' act as a comment when not assigned to a variable and can be used for multiline string

#print multiple variables
a1 = "Ayush"
b1 = "Vaibhav"
c1 = "Aryan"
print(a1, b1, c1) #Ayush Vaibhav Aryan