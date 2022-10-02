'''
The random mamory is volatile and all its content are lost ance program termicates.
Its orders to persits the data forever, we uses files 
A file is a data stored in a storage device. A Pythin program can talk to file by reading content 
from it and writing content to it 
 '''

'''
 Types of files 
There are 2 types of files :
01. Text files (,text, .c, etc.)
02. Binary files (.lpg, .dat, etc.)

Python has a lot of function for reading, updating and deleting files.
'''

# Python has an open() functions for open files. It takes 2 parameters - filename and mate.
    # open("this.text", "r")



# Use open function to read the content of a file

# f = open('sample.txt', 'r')
f = open('sample.txt')      # By default the mode is r
data = f.read()
print(data)
f.close()


# f = open('sample.txt')      # By default the mode is r
# data = f.read(5)            # It will read only first 5 charechters from the file 
# print(data)
# f.close()



##  For creating a file

# fh = open('sample.txt', 'w')
# fh.write('My money is finished')
# fh.closed()
