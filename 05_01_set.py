
'''
Write a program to read the text from a given file 
'poem.txt' and find out whether it contains the word twinkle
'''

fh = open("poem.txt")
t = fh.read()
if 'twinkle' in t :
    print("twinkle is present")
else :
    print('twinkle is not present' )
fh.closed