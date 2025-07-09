# Before running: print should be 34 as the value returned by the function
# is a separate value from the value stored by the variable answer.

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)