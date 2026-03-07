#stores unique elements

a1 = {3, 5, 23, 45, 69, 78}
a2 = {3, 5, 23}

#a1.clear() #set()
#a1.pop() #removes random element
#a1.remove(23) #error raised when given element no found
a1.discard(45) #no error raised
print(a1)
