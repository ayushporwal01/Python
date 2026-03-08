#for loop

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num * i) 

a = [1, 34, 456, 34, 234]

for item in a:
    print(item, end=", ")

#while loop

i = 1
while i <= 10:
    print(i)
    i += 1

while(True):
    x = int(input("enter a number between 1 to 10"))
    print("You entered " + x)
    if(x == 5):
        break