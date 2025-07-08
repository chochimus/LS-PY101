import random
VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'===> {message}')

def display_winner(player, computer):
    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")):
        prompt("You win!")
    elif ((player == "rock" and computer == "paper") or
        (player == "paper" and computer == "scissors") or
        (player == "scissors" and computer == "rock")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

while True:
    prompt(f"Choose one: {", ".join(VALID_CHOICES)}")
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}, computer chose {computer_choice}')
    
    display_winner(choice, computer_choice)

    while True:
        prompt("Would you like to play again (y/n)?")
        response = input().lower()
        if response.startswith('n') or response.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")
    
    if response[0] == 'n':
        break