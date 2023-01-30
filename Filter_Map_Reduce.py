# Filter Map Reduce


# 1. Filter For specific work
def is_even(n):
    return n%2==0

nums = [2,3,4,5,6,4,3,2,5,6,7,9]

# Syntax - filter(function, iterable))

evens = list(filter(is_even,nums))
print(evens)


Output : 
  [2, 4, 6, 4, 2, 6]

# 2. Lambda in Filter


nums = [21,13,4,51,6,24,32,22,5,26,7,9]

# Syntax - filter(function, iterable))

evens = list(filter(lambda n : n%2==0,nums))
print(evens)

Output : 
  [4, 6, 24, 32, 22, 26]

# 3 Map with function

def update(n):
    return n*2

nums = [21,13,4,51,6,24,32,22,5,26,7,9]


evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(update,evens))
print(doubles)

Output : 
  [8, 12, 48, 64, 44, 52]

# 4 Map with filter

nums = [21,13,4,51,6,24,32,22,5,26,7,9]


evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n : n*2,evens))
print(doubles)

Output : 
  [8, 12, 48, 64, 44, 52]


  
  # 5. Reduce

from functools import reduce # reduce is belongs to module functools


def add_all(a,b):
    return a+b

nums = [21,13,4,51,6,24,32,22,5,26,7,9]


evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n : n*2,evens))

sum = reduce(add_all,doubles)

print(doubles)
print(sum)

Output : 
  [8, 12, 48, 64, 44, 52]
228
        


