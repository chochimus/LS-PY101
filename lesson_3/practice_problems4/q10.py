# Before running: Given the description before, I believe this will be True as 42
# will be interned and c and a are referring to the same object.

a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))