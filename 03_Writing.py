'''
Writing Files in Python
In order to write a file, we first open it in write oe append mode after which,
we use the python's f.write() METHODE ato write to the file !
'''
# # write mode will over write on exixting files 
# fh = open("another.txt", 'w')
# fh.write("Please my write something about me")
# fh.close()


## append mode will write again again in the end 
fh = open("another.txt", 'a')
fh.write("Please my write something about me")
fh.close()