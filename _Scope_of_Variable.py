# Scope of Variable

# 1
a = 10 # Outside Variale called Global Variable 

def something():
    a = 15 # Inside Variale called Local Variable 
    print("Inside Function", a)

something()

print("Outside function", a)

**Output**
Inside Function 15
Outside function 10

# 2, If we dont have local variable
a = 10 # Outside Variale called Global Variable 

def something():
    
    print("Inside Function", a)

something()

print("Outside function", a)

**Output**
Inside Function 10
Outside function 10


# 3, If we want to make local variable as global variable
Note - After create Global Variable from Local varibale using below mwthode then we can not make a local varibale with new value - check line 43
a = 10 # Outside Variale called Global Variable 

def something():
    global a # TO make a Global Variable from Local varibale 
    a = 15
    print("Inside Function", a)

    #a = 25 Not possible
something()

print("Outside function", a)

**Output**
Inside Function 15
Outside function 15

# 4, If we want local valriable and at the same time we need global variable into function block

a = 10 

print(id(a))
def something():
    a = 9
    
    x = globals()['a']
    print(id(x))
    print("Inside Function", a)


something()

print("Outside function", a)

**Output**
2708166083088 # Id of a
2708166083088 # Id of X, both showing same id
Inside Function 9
Outside function 10


# 5, Changing value of Global variable without affecting local variable
a = 10 

print(id(a))
def something():
    a = 9
    
    x = globals()['a']
    print(id(x))
    print("Inside Function", a)

    globals()['a'] = 20 # Changing value of Global variable without affecting local variable


something()

print("Outside function", a)

**Output**
2267585708560
2267585708560
Inside Function 9
Outside function 20
