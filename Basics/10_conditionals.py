#If-Else

age = int(input("Enter your age: "))

if(age >= 18):
    print("You are an adult")
else:
    print("You are a minor")


#Match Case

a = 4

match a:
    case 1:
        print("Case 1") 
    case 2:
        print("Case 1") 
    case 3:
        print("Case 1") 
    case 4:
        print("Case 4") 
    case _:
        print("No Match Found")
        