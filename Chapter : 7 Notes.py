__Start : 1. While loop

'''
 Loops - Sometimes we want to repeat a set of statment 
 in our program for instance Print 1 to 1000.
 Loops make it easy for a programmer to tell the computer, 
 which set of instruction to repeat and how !
 '''
 # Types - 1. While loop and 2. for loop

from multiprocessing.resource_sharer import stop


i = 0
while i<10:                     
    print("Yes "+ str(i))
    i = i + 1


# while i<10:                     This loop will not stop 
#     print("Yes")


#     print("Done")


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
__Start : 2. Quize

i = 1   # Print value 1 to 50 
while i<=50:                     
    print("Yes "+ str(i))
    i = i + 1
print("Done")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 3. Print List while loop

fruits = ['Banana', 'Mango', 'Apple', 'Grapes', 'Apple', 'Orange']
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i + 1

# for loop - A for loop is used to iterate through a sequence like list, tuple or string [iterables]

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 4. Print List for loop

# for loop - A for loop is used to iterate through a sequence like list, tuple or string [iterables]

fruits = ['Banana', 'Mango', 'Apple', 'Grapes'] # Same output but in easiest way
for item in fruits:
    print(item)


# Range function in Python 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 5. Range Function

# Range function in Python 
'''
The range in python is used to generate a sequance of number 
We can also specify the start, stop and step - size 
'''
for i in range(8):  # FOr print from 0 to less than 8 
     print(i)
print("Done")

for i in range(1, 8):  # FOr print from 1 to lesthan 8
     print(i)
print("Done")    
for i in range(1, 8, 2):  # FOr print from 1 to lesthan 8 with step 2
     print(i)
print("Done")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 6. for with else

for i in range(10):  
     print(i)
else:
    print("This is inside else of for")

    # The break statement 
    '''
   break is used to come out the loop when encounterd
   It instruct the program to - Exit the loop now
    '''

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 7. Break statement 

for i in range(10):  
    print(i)
    if i == 5 :
        break
else:
    print("This is inside else of for")

# The break statement 
'''
break is used to come out the loop when encounterd
It instruct the program to - Exit the loop now
'''

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 8. continue statement

for i in range(10):  
    if i == 5 :
        continue
    print(i)


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 9. Pass statement

# Pass statenent - Pass is a null statement in python. It instruct to " Do nothing "
i = 4 
if i>0:
    pass
print("Herry is a good boy")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 10 01 Practice

# 01 - Write a program to print multiplication table of a given number using for loop
# num = int(input("Enter the number"))
# for i in range(1,11):
#     print(str(num) + ' X ' + str(i) + " = " + str(i*num))

num = int(input("Enter the number"))
for i in range(1,11):
    print(f"{num}X{i}={i*num}") # F-string

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 10 02 Practice

# Write a program to genrat all the person names stored in a list l1 and with starts with S
l1 = ["Herry", "Shoam", "Sachin", " Rahul"]
for name in l1 :
    if name.startswith("S"):
        print("Hello " + name)


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 10 03 Practice

num = int(input("Enter the number"))
i = 1
while i <= 10 :
    print(f"{num} X {i} = {num*i}")
    i = i + 1


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 10 04 Practice

# 04 Write a program to find wheather a given number is prime or not
num = int(input("Enter numbers\n"))
prime = True
for i in range (2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 10 05 Practice

# Write a program  to find the sum of first n natural numbers using while loop
num = int(input("Enter the numbers\n"))
sum=0
i=1
while i<=num:
      sum=sum+i
      i=i+1
print(f"The sum of first {num} natural numbers is {sum}")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 10 06 Practice


from asyncore import loop


# Write a program to calculate the factorial of a given numbers using for loop 

num = int(input("Enter the numbers\n"))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print((f"THe factorial of {num} is {factorial}"))

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 10 07 Practice

# Write a program to print tha following pattern
'''
   *
  ***
 ******
for n = 4
'''
n = 3
for i in range(3):
    print(" " * (n-i-1), end= "")
    print("*" * (2*i+1), end= "")
    print("" * (n-i-1))


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 10 08 Practice

# Write a program to print tha following pattern
'''
*
**
***
for n = 4
'''

n = 4

for i in range(4):
    print("*"*(i+1))

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 10 09 Practice

num = int(input("Enter the number"))
for i in reversed(range(1,11)):
    print(f"{num}X{i}={i*num}") # F-string


    

# num = int(input("Enter number: "))
# for i in range(0,10):
# 	print(str(num)+' X '+str(10-i)+' = '+str(num*(10-i)))

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
