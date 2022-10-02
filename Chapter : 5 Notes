__Start - 01. Dictionary

# A Dictionary is a collection of key value pairs.
# Properties of Dictionary 1. It is unorderd, 2. It is mutable, 3. It is indexced 

myDict={"Fast" : "in a quick manner", 
"Harry" : "a coder",
"Number" : [23,44,43],
"anotherdict" : {'Tarun' : 'Python'}
}
print(myDict['Fast'])
print(myDict['Harry'])
myDict['Number'] = [22,43] # Can change dictionary 
print(myDict['Number'])
# print(myDict['anotherdict'])
print(myDict['anotherdict']['Tarun'])

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start - 01. Dictionary Methods

myDict={"Fast" : "in a quick manner", 
"harry" : "a coder",
"number" : [23,44,43],
"anotherdict" : {'Tarun' : 'Python'},
1:3
}
print(myDict.keys())    # Prints the keys of the dictionary
print(myDict.values())  # Prints the values of the dictionary
print(myDict.items())   # Pritn the (key, value) for all the contents of the dictionary
print(myDict)
updateDict = {
    "Hate" : "Love"
}
myDict.update(updateDict) # Update the Dictionary by the adding key-value pairs from updateDict
print(myDict)

print(myDict.get('harry'))  # Prints values associated with key "herry"
print(myDict['harry'])      # Prints values associated with key "herry"

## The difference between .get and [] syntex in Dictionaries ?
print(myDict.get('harry1')) # Returns Nons as herry1 is not present in the dictionary
print(myDict['harry1'])     # Throw an error as herry1 is not present in the dictionary

## More methodes are available on docs.python.org

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start - 03. Set

# Set is a collection of a non repetitive elements 

a = {1,2,3,4,5,6,7,8,9,1,2,3,1}
print(a)
print(type(a))

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start - 04. 

# Important : This syntax will create an empty dictionary and not an empty set 
a = {}
print(type(a))

# THe empty set can be created by using the below syntex : 
b = set()
print(type(b))

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start - 05. Sets Nethods

# creating an empty set 
b = set()
print(type(b))

# Adding values to an empty set 
b.add(4)    # Adding a value repeatedly does not changes a set 
b.add(4)
b.add(9)
b.add((23,34))

# b.add([23,34])    # Cannot add list or dictionary to set 
# b.add({23:34})
print(b)

print(len(b))   - # Prints the length of this set 
b.remove(4)       # remove 4 from this set b 
# b.remove(13)    # throw an error while trying to remove 13 ( Which is not present in the set )
print(b.pop())
print(b)

'''Properties of set 
01 Sets are unorderd 
02 Sets are unindexed 
03 Ther is no way to change item in sets 
04 Sets can not contain duplicate values 
'''

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start - 06. Practice 1

# 01 Write a program to create a Dictionary of Hindi words with values as their english translation. Provide user with an option to look it up !
mydict = {
    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Vastu" : "Item"
}
print("Options are ", mydict.keys())
a = input("Enter the Hindi Word\n")
# print("The meaning of your word is: ", mydict[a])
# Below line will not throw an error if the key is not present in the dictionary 
print("The meaning of your word is: ", mydict.get(a))

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start - 06. Practice 2

# 02 Write a progrsm to input eight numbers from the user and display all the unique numbers(once)
# alt + shift select first and last 
from hashlib import shake_128


num1 = int(input("Enter number 1\n "))
num2 = int(input("Enter number 2\n "))
num3 = int(input("Enter number 3\n "))
num4 = int(input("Enter number 4\n "))
num5 = int(input("Enter number 5\n "))
num6 = int(input("Enter number 6\n "))
num7 = int(input("Enter number 7\n "))
num8 = int(input("Enter number 8\n "))
s = {num1, num2, num3, num4, num5, num5, num6, num7, num8}
print(s)


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start - 06. Practice 3

# Can we have a set with 18(int) and "18"(str) as a value in it ?
s = { 18, "18"}
print(s)


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start - 06. Practice 4

# What will the length of following set 5
'''
s = set()
s.add(20)
s.add(20.0)
s.add("20")
'''

s = {20, 20.0, "20"}
print(len(s)) # here set count 20 and 20.0 as same 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


__Start - 06. Practice 5

# what is type of given s
s = {}
# Ans
print(type(s)) # its a dictionary

# Note : s = set() its a empty set

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


__Start - 06. Practice 6

'''Create an empty dictionary. Allow 4 friends to enter their 
favourite language as a values and uses keys as their names. Assume that the names are unique.'''

favlang = {}
a = input("Enter your favourite language Subham\n")
b = input("Enter your favourite language Ankita\n")
c = input("Enter your favourite language Raveena\n")
d = input("Enter your favourite language Nimbus\n")
favlang["Subham"] = a
favlang["Ankita"] = b
favlang["Raveena"] = c
favlang["Nimbus"] = d
print(favlang)
