#A dictionary is a collection of key-value pairs.
#Each value is associated with a unique key. 
#Mutable

dict1 = {}
print(type(dict1))                  #<class 'dict'>

marks = {"Ayush": 69, "Rahul": 54, "Akshat": 74, "Vaibhav": 91}
marks2 = {"Akshat": 88, "Rahul": 99}

print(marks["Ayush"])

marks["Aryan"] = 58
print(marks)      

print(marks.get("Ayush Porwal"))    #None
print(marks.get("Ayush"))           #69
print(marks.keys())   
print(marks.items())   

marks.pop('Ayush')   
print(marks)  

print(marks.popitem())              #Removes and returns last item as a tuple

marks.update(marks2)                #Before: {'Rahul': 54, 'Akshat': 74, 'Vaibhav': 91}
print(marks)                        #After: {'Rahul': 54, 'Akshat': 74, 'Vaibhav': 91}