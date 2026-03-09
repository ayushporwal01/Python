#exception handling is a way to handle errors that occurs during program execution.

try:
    a = int(input("Enter a number: "))
    print(a + 3)
except Exception as e:
    print("some error occured: ", e)