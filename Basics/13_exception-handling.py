#exception handling is a way to handle errors that occurs during program execution.
#try - code that may cause error
#except - runs if error occurs
#else - runs if no error occurs
#finally - runs whether error occurs or not

#Common Python Exceptions
#ZeroDivisionError – dividing by zero
#ValueError – invalid value
#TypeError – wrong data type
#IndexError – list index out of range
#FileNotFoundError – file not found

try:
    a = int(input("Enter a number: "))
    print(a + 3)
except Exception as e:
    print("some error occured: ", e)
else:
    print("no error occurred")
finally: 
    print("always runs")   
   