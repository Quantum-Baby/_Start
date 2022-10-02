 ## With statement 
'''
The best way to open and close the file automaticaly is the with statement 
with open("text.txt") as f :
f.read()
'''
with open("another.txt", 'r') as f :
    a = f.read()
print(a)