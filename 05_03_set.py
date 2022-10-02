'''
Write a program ti generate multipication tables 2from 2 to 20 
and write it to the differnt files. Place these files in a folders 
for a 13 year old
'''

for i in range(2,21) :
    with open(f"tables/Multilpication_table_of_{i}.txt", "w") as f:
        for j in range(1,11):
            f.write(f"{i}X{j} = {i*j}")
            if j!=10:
                f.write('\n')
