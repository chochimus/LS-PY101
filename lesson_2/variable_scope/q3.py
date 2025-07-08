# Before running: I believe this code will print 10 as the global
# keyword causes the variable used in my_func to be the global num.

num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

# prints 10