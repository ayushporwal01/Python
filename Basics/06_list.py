#A list is an ordered collection of items.
#Mutable
#Can store mixed types of values


l1 = [1, 4, 3, 3, "Ayush", 2, 5]

print(type(l1)) #<class 'list'>
print(l1) #1 4 3 3 'Ayush' 2 5 

print(l1[1:4]) #4 3 3

l1.remove("Ayush")
print(l1) #1 4 3 3 2 5

print(l1.count(3)) #2

l1.sort()
print(l1) #1 2 3 3 4 5

l1.pop()
print(l1) #1 2 3 3 4

l1.append(10)
print(l1) #1 2 3 3 4 10

print(l1.index(3)) #2

l1.extend([100, 69, 11, "Vaibhav"])
print(l1) #1 2 3 3 4 10 100 69 11 'Vaibhav'

l1.clear()
print(l1) #[]
