name = "satyam"
print(name)

name2 = 'Satyam'
print(name2)

print(name[0:3]) #--> to get character out of string start from 0 and go till 2(3-1)
print(name[2:5])# --> start from 2 index and go till 4 index(5-1)

print(name.capitalize())
print(name.upper())
print(name.count("a"))
print(name.isalnum()) #--> is alphanumeric
print(name.isnumeric())#--> is numeric or not

a1 = "Satyam"

a2 = 'Satyam'

a3 = '''Hey how are  you
this method is used for multi
line typing in string'''

print(a1 + "\n" + a2 + "\n" + a3)

# Strings are immutable --> can't be changed --> i.e name[0:3] is a new string made by python

