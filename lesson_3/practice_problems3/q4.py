# Before running: I believe element 0 of my_list1 will be {"first": 42} as .copy()
# only performs a shallow copy

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)