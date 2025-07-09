# Before running: bar(foo()) -> bar("yes") -> returns False and (True or no)
# short circuits to False

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

print(bar(foo()))