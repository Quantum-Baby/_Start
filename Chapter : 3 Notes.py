__Start - String

## String - String is a data type in Python, String is a sequance of charecter enclosed in qutoes 
from ctypes import FormatError
from traceback import print_tb
from turtle import st


a = 'Tarun'
b = "Nakku"
c = '''Like'''
print(a)
print(b)
print(c)

A = "Hery's"
print(A)
print(type(A))
B = '''I am not a 
Good Boy'''
print(B)

greeting = "Good Morning "
Name = "Tarun" 

# Concatenating two string
c = greeting + Name 
print(c)

print(Name[4])
# Name[3] = "d" --> Does not work, Because string is unmutable

print(Name[1:4])    # String slicing 
print(Name[ :4])    # is same as print(name[0:4])
print(Name[0:])     # is same as print(name[0:5])
print(Name[-4:-1])  # is same as print(name[1:4])

## Slicing with skip value
d = "Loveisblind"
print(d[1:8:2])


## Sting Function
story = "a man is in love with a cute girl and that girl is osm"
print(len(story))                              # len - give the length of string
print(story.endswith("osm"))      # endswith tell us that string is end with which string and give True and False
print(story.endswith("hot girl"))
print(story.count("girl"))              # count tell how many time a string is coming 
print(story.capitalize())               # capitalize is used to capitalize first letter 
print(story.find("girl"))               # find will find the position of string(here girl's first occurance will come only)
print(story.replace("man", "godd man"))  # replace is used for replacing the string(it will replace all occurance if any )


# escape sequance 
m = "Tarun is \nstarting \tlearning pythong "  #  \n is escape sequance using for print in a new line and \t is used for add tap \' will give quote and \\ will add \  etc, '''
print(m)


# ************End of String***************

# # 01 Create a programme 
# name = input("Enter your name : ")
# print("Good afternoon, " + name )

# # 02
# letter = '''Dear <|Name|>
# you are selected 
# Date : <|Date|>
# '''
# name = input("Ente your name\n")
# date = input("Enter Date\n")
# letter = letter.replace("<|Name|>", name)
# letter = letter.replace("<|Date|>", date)
# print(letter)



# love = ('''My love name is <|Name|>
# She is cute and I love her sooooo much 
# We were first meat on the day of <|Date|>
# She is every thing for me 
# I will surly proposed her near <|Place|>.''')

# name = input("Enter her Name : ")
# date = input("Enter the date when u were meat with her for the first time : ")
# place = input("Enter the place name : ")

# love = love.replace("<|Name|>", name)
# love = love.replace("<|Date|>", date)
# love = love.replace("<|Place|>", place)
# print(love)

## 03 Create programme to detect a double space from a sting 

# st = ("The name of my is Tarun")
# doublespaces =st.find("  ") 
# print(doublespaces)

## 04 replace doublespaces with single spaces
# st = ("The name of my is  Tarun")
# st = st.replace("  ", " ") 
# print(st)

##05 
# letter =  "Dear Tarun, This python cource is nice ! Thanks"
# print(letter)
# Formatleter = "Dear Tarun, \n\tThis python cource is nice ! \nThanks"
# print(Formatleter)
