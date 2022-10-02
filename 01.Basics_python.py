print("Helow World")
## Data type in PYTHON
# None, Numeric, List, Tuple, Set, String, Range and Dictionary

# None : When we have a Variable with no value assign to this we called None

# Numeric : int, float, complex, and bool , Example
num = 2.5
print(type(num))
num = 5 
print(type(num))
num = 9+2j
print(type(num))
 # We can change the type
a = 5.6
b = int(a)
print(b)

# Bool is for True and False
c = a<b
print(bool(c))

# In python True as 1 and False as 0
print(int(True))
print(int(False))

#type
A = [23, 33,21, 45]
print(type(A))
B = (22,23,12)
print(type(B))
C = {33,9,99}
print(type(C))
str = "naveen"
print(type(str))

# Range
print(range(0,10))
print(list(range(0,10)))
#Range can does 3 parameters as well like we want only prime numbers from list we can do this like from 2 to 10 and difference is 23
print(list(range(2,10,2)))
print(type(range(10)))

# Dictionary : we have key here, key should be unique but value can be repeated 
d = {'naveen': 'samsung', 'rahul': 'Iphone'}
print(d)
print(d.keys())
print(d.values())
print(d['rahul'])
#or
print(d.get('rahul'))

Data = {1:'Naveen', 2:'Tarun', 4:'Name'}
print(Data[4])
print(Data.get(3, 'Not Found'))

# Create list and cretae Dictionary with it 
keys = ['Naveen', 'Tarun', 'Kiran']
values = ['Python', 'Java', 'No']
dato = dict(zip(keys,values))
print(dato)
