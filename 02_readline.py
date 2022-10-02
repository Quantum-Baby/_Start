# READ FIRST LINE 
f = open('sample.txt', 'r')
data = f.readline()
print(data)

# READ SECONND LINE 
data = f.readline()
print(data)

# READ THIRD LINE 
data = f.readline()
print(data)

# READ FORTH LINE 
data = f.readline()
print(data)

# READ FIFTH LINE...... AND SO ON.......
data = f.readline()
print(data)
f.close()