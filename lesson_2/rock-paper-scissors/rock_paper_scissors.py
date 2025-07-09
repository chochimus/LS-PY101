import random
VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']
ABBREVIATIONS = {
        'r': 'rock',
        'p': 'paper',
        'sc': 'scissors',
        'sp': 'spock',
        'l': 'lizard'
}
WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

def prompt(message):
    print(f'===> {message}')

def player_wins(player, computer):
    return computer in WINNING_COMBOS[player]

def resolve_choice(input_str):
    if input_str in VALID_CHOICES:
        return input_str
    if input_str in ABBREVIATIONS:
        return ABBREVIATIONS[input_str]
    return None

def get_winner(player, computer):
    if player_wins(player, computer):
        return "player"
    if player == computer:
        return "tie"

    return "computer"

def display_winner(winner):
    if winner == "player":
        prompt("You win!")
    elif winner == "computer":
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

while True:
    player_score = 0
    computer_score = 0

    prompt('Best of 5, first to 3 wins')

    while player_score < 3 and computer_score < 3:
        prompt(f'Score: P - {player_score} C - {computer_score}')
        prompt(f"Choose one: {", ".join(VALID_CHOICES)}")
        choice = resolve_choice(input())

        while choice is None:
            prompt("That's not a valid choice")
            choice = resolve_choice(input())

        computer_choice = random.choice(VALID_CHOICES)

        prompt(f'You chose {choice}, computer chose {computer_choice}')

        current_winner = get_winner(choice, computer_choice)
        display_winner(current_winner)

        if current_winner == "player":
            player_score += 1
        elif current_winner == "computer":
            computer_score += 1

    prompt(f'Final Score: P - {player_score} C - {computer_score}')
    if player_score == 3:
        prompt("You are the GRAND WINNER!")
    else:
        prompt("Computer is the GRAND WINNER!")

    while True:
        prompt("Would you like to play again (y/n)?")
        response = input().lower()
        if response.startswith('n') or response.startswith('y'):
            break

        prompt("That's not a valid choice")

    if response[0] == 'n':
        break