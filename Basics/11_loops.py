#for loop

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num * i) 

a = [1, 34, 456, 34, 234]

for item in a:
    print(item, end=", ")

# #while loop

i = 1
while i <= 10:
    print(i)
    i += 1

while(True):
    x = int(input("enter a number: "))
    if(x == 69):
        print("you won")
        break
    else:
        print("Try again!")

while i <= 10:
    if i == 5:
        i += 1
        continue

    print(i)
    i += 1
    