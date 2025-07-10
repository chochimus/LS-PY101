# Before running: My IDE gives this problem away but no, the second return statement
# returns nothing as the block isn't on the same line as the return so it is never used.
# The first statement returns as expected.

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())