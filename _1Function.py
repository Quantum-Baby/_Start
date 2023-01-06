# Function

'''
Syntax-

def greet(): 
    print() # block of function

greet() # calling funcation
    
'''
#1
def greet():
    print("Hello")
    print("My name is tarun")

greet()

#2
def add(x,y):  # x,y is Arguments / paramenters
    c = x+y
    print(c)

add(3,4)

#or
def add(x,y):  
    c = x+y
    return c

result = add(3,4)
print(result)

#3
def add_sub(x,y):  
    c = x+y
    d = x-y
    return c,d

result1,result2 = add_sub(3,4)
print(result1,result2)

#4 Pass by value or pass by reference

# def update(x):
#     x = 8 # will tske only 8 because we updated value here 
#     print(x)

# update(10)

# # OR 

# def update(x):
#     x = 8 # will tske only 8 because we updated value here 
#     print("x", x)

# a = 15
# update(a)
# print("a", a
# 

'''
Function argument

def add(a,b):  # a,b is Formal arguments
    c = a + b
    print(c)

add(5,6) # 5,6 is Actual arguments

## Actual arguments has four types
1. Position
2. Keyword
3. Default
4. Variable length
'''

# Position
def add(name, age): 
    print(name)
    print(age)

add("naveen",23)

# Keyword
def add(name, age): 
    print(name)
    print(age)

add(age = 28, name = "Tarun")

# Default
def add(name, age = 18): 
    print(name)
    print(age)

add("Arun")

# Variable length
def add(a,*b): 
    c = a
    for i in b:
        c = c+i
    print(c)

add(7,3,2,1,2,3,88)

# or

def add(*b): # Length
    c = 0
    for i in b:
        c = c+i
    print(c)

add(7,11,1,2,3,88)


# We have another Argument - Keyworded Variable Length Arguments in Python | **kwargs

def person(name, *data):
    print(name)
    print(data)

person("Tarun", 23, "India", 909889)

#  ***Output***
Tarun
(23, 'India', 909889)  # But here we dont know about (23, 'India', 909889) that what they represent.

# Accurately work with -> Keyworded Variable Length Arguments in Python | **kwargs

def person(name, **data):
    print(name)
    print(data)

person("Tarun", age = 23, Country = "India", Phone_No = 909889)

#  ***Output***
Tarun
{'age': 23, 'Country': 'India', 'Phone_No': 909889}

# Using Loop -> Keyworded Variable Length Arguments in Python | **kwargs

def person(name, **data):
    print(name)

    for i,j in data.items():
        print(i, j)

person("Tarun", age = 23, Country = "India", Phone_No = 909889)

#  ***Output***
Tarun
age 23
Country India
Phone_No 909889
