# Before running: line 7 will print [1, 2]
# line 8 will print {'first': [1, 2]}
# num_list is just a reference to the list in the dictionary so modifying it
# will also modify the contents of first in dictionary

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)