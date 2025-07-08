# Before running: My IDE gives this one away but there will be a NameError 
# as, the num in the print call hasn't been created as the num in my_func is local
# only to the function.

def my_func():
    num = 10

my_func()
print(num)

# NameError