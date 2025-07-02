def prompt(message):
    print(f'==> {message}')

prompt('Welcome to Calculator!')

prompt("What's the first number?")
number1 = int(input())

prompt("What's the second number?")
number2 = int(input())

prompt('What operation would you like to perform?\n'
       '1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

match operation:
    case '1':
        output = number1 + number2
    case '2':
        output = number1 - number2
    case '3':
        output = number1 * number2
    case '4':
        output = number1 / number2

prompt(f'The result is: {output}')

