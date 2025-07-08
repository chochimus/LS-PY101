# Before running: This code should print Inner 1: 25 then Inner 2: 15 on the next line.
# This is because inner_func1 creates a local var x = 25, while inner_func2 uses the
# x variable initialized in my_func.

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# prints 
# Inner 1: 25
# Inner 2: 15