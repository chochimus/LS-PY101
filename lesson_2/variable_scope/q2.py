# Before running: This code will print 5 as the assignment in my_func
# creates a local variable, while the print is accessing the global num

num = 5

def my_func():
    num = 10

my_func()
print(num)

# prints 5