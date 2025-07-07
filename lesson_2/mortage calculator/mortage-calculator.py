def prompt(message):
  print(f'=> {message}')

def valid_float(input):
  try:
    float(input)
  except ValueError:
    return False
  return True

def get_valid_float(prompt_message):
  prompt(prompt_message)
  number = input()
  while not valid_float(number):
    prompt(f'invalid input: you entered {number}, try again')
    prompt(prompt_message)
    number = input()
  return float(number)


prompt('Welcome to Mortgage Calculator!')

while True:
  loan_amount = get_valid_float('Enter your loan ammount (e.g. 100.00): ')
  apr = get_valid_float('Enter your APR percent (e.g 12.5 for 12.5%): ') / 100
  loan_years = get_valid_float('Enter loan duration in years: ')
  loan_duration = (loan_years  * 12)
  interest_rate = apr / 12

  if(apr == 0):
    result = loan_amount / loan_duration
  else:
    result = loan_amount * (interest_rate / (1 - (1 + interest_rate) ** (-loan_duration)))
  prompt(f'Your monthly payment will be: ${result:.2f}')

  prompt('Would you like to perform another calculation (y/n)?')
  answer = input().lower()
  while answer not in ["y", "n"]:
    prompt('answer should be single letter y or n')
    prompt('Would you like to perform another calculation (y/n)?')
    answer = input()
  if answer == "n":
    break