# Before running: I believe this code will print 5 when called
# as the num variable printed will be the global num as there is 
# no local assignment done

num = 5

def my_func():
    print(num)

my_func()

# prints 5