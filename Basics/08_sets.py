#stores unique elements
#unordered
#mutable

a1 = {3, 5, 23, 45, 69, 78}
a2 = {3, 5, 23, 7, 100}

#a1.clear()                   #set()
#a1.pop()                     #removes random element
#a1.remove(43)                #error raised when given element not found
#a1.discard(45)               #no error raised

#res = a1.difference(a2)      #intersection

#a1.add(7)                    #adds given ele in a random place if it's not already present
 
#a3 = a1.copy()     
#a4 = a1.union(a2);            

#print(a2.issubset(a1));                 
#print(a1.issuperset(a2));       
          
a1.update(a2);                #copies all elements of a2 in a1 
print(a1);                    #a1 + a2
print(a2);                    #remains same

