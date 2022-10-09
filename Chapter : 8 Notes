__Start : 01 Function

# A function is a grop of statement performing a specific task.
# When a program gets bigger in size and its complexity grows, it gets difficults for a programmer to keep track on which pprogramm of code is doing what 
# A function can be reused by the programmer in a given program any nuber of any number of time


# marks1 = [36,78,54,78]
# percentage1 = ((marks1[0]+marks1[1]+marks1[2]+marks1[3])/400)*100 # When u dont know about sum functions 


# marks2 = [ 36,78,54,78]
# percentage2 = (sum(marks2)/400)*100  # When u know about functions 
# print(percentage1, percentage2)


def percent(marks):
    p =((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p

marks1 = [16,71,24,8]
percentage1 = percent(marks1)

marks2 = [32,32,32,32]
percentage2 = percent(marks2) 
print(percentage1, percentage2)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
__Start : 02. 

# Quick Quize - Write a program to create a user with "Good by" using function



def greet(name):
    print("Good Morning," + name)

greet("Tarun")
greet("Goku")

# Types of Function 
# 01 Build in function - Already present in Python 
# 02 User defined function - Defined by the user


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
__Start : 03

# Default argument - We can have a values as default argument in a function.

def greet(name = " Stranger "):
    print("Good Morning," + name)

greet("Tarun")
greet("Goku")
greet()

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
__Start : 04

# Recursion is a function which call itself , It is used to directly use a mathematical formula as a function.
# for ex. - factorial(n) = n * factorial(n-1)
# This function can be defined as follow 
# def factorial(n):
#     if i == 0 or i == 1
#     return 


# n = 5
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)




# n! = 1*2*3*4*5*6*n
# n! = n*(n-1)!

# def factorial_iter(n):              # iter - itreative factorial method which is calculating factorial by loop
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product

# f = factorial_iter(5) 
# print(f)



def factorial_recursive(n):   # recursive is use only when formulas related 
    if n == 1 or n == 0 :
        return 1
    return n * factorial_recursive(n-1)

f = factorial_recursive(5) 
print(f)

'''
A programmer need to be externally careful while working to ensure that the 
function does not infinitely keep calling itself 
Recursion is sometimes the most direct way to code an algorithm
'''


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
__Start : 05 Practice - 1

# 01 Write a program using function to find greater of three numbers 



from importlib import machinery


def maximum(num1, num2, num3):
    if (num1>num2) :
        if (num1>num3):
            return num1
        else :
            return num3
    else:    
        if (num2>num3):
            return num2
        else :
            return num3
m = maximum(23,56,5)
print(m)
        




-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
__Start : 06 Practice 2

# 02 Write a program using function to convert celsius to farnehit

from calendar import c


def farh(cel):
    return (cel * (9/5)) + 32
c = 45
f = farh(c)
print("Farnehite Temprature is " + str(f))


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
__Start : 07 Practice 03

# 03 How do you prevent a python print() function to print a new line at the end

print("Hello", end = " ")
print("My", end = " ")
print("Name" , end = " ")
print("is", end = " ")
print("Tarun", end = " ")


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
__Start : 08 Practice 04

# 04 Write a recurcive function to calculate  the sum of sirst n natural numbers

def sum_recursive(n):
    if n == 0 or n == 1 :
        return 1
    return n + sum_recursive(n-1)

f = sum_recursive(7) 
print(f)


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
__Start : 09 Practice 05

'''05 - Write a python function to print first n lines of the following pattern
***
**
*
for n = 3
'''

n = 3
for i in range(n):
    print("*" * (n-i))

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
__Start : 10 Practice 06

# 06 Write a python function which convert inches to cms


def centimeter(inch):
    return(inch*2.54)

i = 1
c = centimeter(i)
print(c)



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
__Start : 11 Practice 07

# 07 Write a python function to remove a given word from a string and step it at the same time.

def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.split()


this = "    popo is not Good    "
n = remove_and_split(this, "popo")
print(n)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
__Start : 12


# Build a basic calculator

from tkinter.colorchooser import Chooser

# def sum(a,b):
#     return a + b

# def sub(a,b):
#     return a-b
    
def mul(a,b):
    return a*b

# def div(a,b):
#     return a/b
    
a = int(input("Enter first number : "))
b = int(input("Enter second number : " ))

sum1 = mul(a,b)
print(sum1)


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
