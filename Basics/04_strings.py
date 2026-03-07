name = 'Ayush'
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