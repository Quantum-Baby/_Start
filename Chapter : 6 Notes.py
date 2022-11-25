__Start : 1 Conditional Expression 

# Conditional Expression 
# If, else and elif steatement are a multiway decission taken by our program due to certain conditaions in our code.

a = 50

# if-elif-else ladder in Python 
# if(a>45):
#     print("THe value of a is greater than 45 ")
# elif(a>23):
#     print("The value of a is greater than 23")
# elif(a>3):
#     print("The value of a is greater than 3")
# else:
#     print("The value of a is not greater than 23 or 45")

if(a>45):
    print("The value of a is greater than 45 ")

if(a>35):
    print("The value of a is greater than 35 ")

if(a>34):
    print("The value of a is greater than 34 ")


if(a>75):
    print("The value of a is greater than 75 ")
elif(a>23):
    print("The value of a is greater than 23")
elif(a>3):
    print("The value of a is greater than 3")
else:
    print("The value of a is not greater than 23 or 45")
    
print("Done")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 2. if, else quize

''' Quick Quize = Write a program to print yes when the age 
    entered by the user is greater than or equal to 18 '''

Age = int(input("Input here your age here : "))

# if(Age>18):
#     print("Yes")
# elif(Age<18):
#     print("No")
# else:
#     print("The age of tarun is not greater than 18")
    
    
if Age>18 :
    print("Yes")
elif Age<18 :
    print("No")
else:
    print("The age of tarun is not greater than 18")
    

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 3. LOgical and relational operator

'' 
Relational Operator_ Relational Operator are 
used to evaluate conditions inside the if statements.
Ex : 
== - equal, >= - greater and equal, <= - lesthan equal, etc.
'''

''''
Logical Operator - In python logiccal operators operat on Conditionl statements.
EX :
and - true if both operators are true else false
or - true if at least an operators are true else false
not - inverts true to false and false to true
'''

age = int(input("Entre your age : "))

# if(age>34 and age<56):
#     print("You can work with us")
# else:
#     print("You can not work with us")


# if(age>34 or age<56):
#     print("You can work with us")
# else:
#     print("You can not work with us")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 4. in-and-is

a = None
if a is None :
    print("Yes")
else :
    print("NO")

A = [23,43,23,22]
print(23 in A)
print(33 in A)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 5. Practice - 1

# Write a program to find greater of four numbers enter by users
num1 = int(input('Enter number 1 : '))
num2 = int(input('Enter number 2 : '))
num3 = int(input('Enter number 3 : '))
num4 = int(input('Enter number 4 : '))

if(num1>num4):
    f1 = num1
else:
    f1 = num4
if(num2>num3):
    f2 = num2
else:
    f2 = num3
if(f1>f2):
    print(str(f1) + "is greater")
else:
    print(str(f2) + "is greater")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 6. Practice - 2

Sub1 = int(input('Enter first subject marks\n'))
Sub2 = int(input('Enter second subject marks\n '))
sub3 = int(input('Enter third subject marks\n'))

if(Sub1<33 or Sub2<33 or sub3<33):
    print("You are fail becaue u have less than 33% marks in one of subjects")
elif(Sub1+Sub2+sub3)/3 < 40 :
    print("You are fail due to total percentage less than 40")
else:
    print(" Congratulation you are passed")
    
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 7. Practice - 3

'''
A spam comment is defined as a text containing following keywords

"made a lot of money", " buy now", "click this", "subscribe this".
'''

text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else: 
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


__Start : 6. Practice - 4. 

# Self ans of this question - Write a program to find wheather a given usernaamw contain less than 10 charecter or not

username = input("Enter your user name : \n")
#print(len(username))
if(len(username)<10):
    print("Yes , Length of username is less than 10")
else:
    print("No, Length of username is not less than 10")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 6. Practice - 5.

# Write a program which find out wheather a given name is present in a list or not.
names = ['herry', 'Nnu', 'Tarun', 'Kakul', 'Puja']
nam = input("Enter your name\n")
if nam in names :
    print("Your name is present in list")
else:
    print("Your name is not present in list")
    
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

__Start : 6. Practice - 6.

'''
Write a program to calculate the grade of a student from 
his marks from the following scheme :
90-100 = Ex
80-90 = A
70-80 = B
60-70 = C
50-60 = D
< 50 = F
'''

marks = int(input("Enter your marks\n"))
if marks>=90:
    grade = "EX"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D"
else:
    grade = "f"
print("Your grade is "+ grade)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
