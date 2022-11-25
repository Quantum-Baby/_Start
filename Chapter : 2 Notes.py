_Start - 01 - Variable and Datatype

## Variable - Variable is like a container and it can use for store data in memory somewhere. 
# Note : Variables are case sensitives, Eg - A and a
  ## Keyword - Reserved word in Python
  ## Identifires - class/function/variable name
  
a = 'Naveen'
b = '''Tarun
is
a 
Bad
boy'''
c = 234.4    
d = True
e = None    


## Data type in PYTHON
# None, Numeric, List, Tuple, Set, String, Range and Dictionary

# Printing the variable 
print(a)
print(b)
print(c)
print(d)
print(e)
# Printing the type of variable
print(type(a))
print(type(c))
print(type(d))
print(type(e))


### 02. Operators

# Arithmetic operator

A = 2
B = 4
print("The value of 2+4 is", 2+4) 
print("The value of 2-4 is", 2-4)
print("The value of 2\4 is", 2/4)
print("The value of 2*4 is", 2*4)

# Assignment operator

a = 34
a += 12
a -= 12
a /= 12
a *= 12
print(a)

# Comparision operator
m = 3>4
print(m)

# Logical operator
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The value of bool1 is not bool2 ", (not bool2))

## Type function and type casting
x = '90'
x = int(x)
print(x)
print(type(x))
print(x + 3)

z = 30
n = str(z)
print(n)
print(type(n))

# A string can be convert into int or vice versa if possible


# Will show error bcs string cant be a int form 
# x = '90A'
# x = int(x)
# print(x)
# print(type(x))
# print(x + 3)

#### @ Input function _ Go to code - _input_function

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
_Start - 02

''' input = This function is allows the user to take input from the keyword as a string-
 It is important to note that the output of input is always a string (even if number is enter)'''


a = input('Enter your good number : ') 
a = int(a)  # Convert a to an Integer(if possible)
print(type(a))

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start - 03 Practice 

# 01 Create a python programe for add 2 numbers

from ast import operator

a = 458
b = 15
print("The sum of a and b is", a + b)

        OR
        
a = int(input("Enter first Number : \n "))
b = int(input("Enter second Number : \n "))
sum = a+b
print("The sum of two number " , sum)

# 02 For remender
print("The remainder when a is devided by b is", a % b)

# 03 comparision 
a = 34
b = 80
print(a>=b)

# For avarage
print("The avarage  of  a and b is", (a + b)/2)

# ## for avarage but take number from user
# x = input("Enter first number")
# y = input("Enter second number")
# x = int(x)
# y = int(y)
# avg = (x+y)/2
# print("The avarage  of  x and y is", avg)

# ## for square but take number from user
# m = input("Enter number : ")
# m = int(m)
# square = (m**2)
# print("The square  of  m is", square)
