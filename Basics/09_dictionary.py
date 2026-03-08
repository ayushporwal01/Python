#A dictionary is a collection of key-value pairs.
#Each value is associated with a unique key. 
#Mutable

dict1 = {}
print(type(dict1))                  #<class 'dict'>

marks = {"Ayush": 69, "Rahul": 54, "Akshat": 74, "Vaibhav": 91}

print(marks["Ayush"])

marks["Aryan"] = 58
print(marks)      

print(marks.get("Ayush Porwal"))    #None
print(marks.get("Ayush"))           #69
print(marks.keys())   