l1 = [1, 2, 3, 3, "Ayush", 4, 5]

print(type(l1)) #<class 'list'>
print(l1) #1 2 3 3 'Ayush' 4 5 

l1.remove("Ayush")
print(l1) #1 2 3 3 4 5

print(l1.count(3)) #2