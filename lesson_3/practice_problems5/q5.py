# Before running: IDE gives these type of questions away, but the greeting in the if
# block is never instantiated because the block isn't executed so it will cause a NameError

if False:
    greeting = "hello world"

print(greeting)