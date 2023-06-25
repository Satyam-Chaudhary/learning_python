#can have multile datatpes --> not like array
l1 = [3, 7, 7, 5, 2, 7, 4 ,"Satyam"]
print(type(l1))
print(l1)

#lists are not immutable i.e can be changed doesn't make a new datatype like strings

l1.remove("Satyam")
print(l1) #--> l1 is printed after changed
print(l1.count(7))
l1.sort()
print(l1)
l1.pop()
print(l1)
l1.append(1)
print(l1)
print(l1[0:3])
l1.extend([1, 2, 3 ,4 ,5])
print(l1)
print(l1.index(7))
l1.clear()
print(l1)
