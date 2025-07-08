# Before running: I believe this code will print Hello World as
# the inner function should have access to the outer_var.

def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# Prints Hello World