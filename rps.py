import random

def get_user_input():
    valid_inputs = ['r', 'p', 's', 'q']
    user_input = ''
    while user_input not in valid_inputs:
        user_input = input("Rock (r), Paper (p), Scissors (s), or Quit (q)?\n")


    return user_input

# Fix the error in this code!
def get_computer_input(i):
    # key-value pair
    computer_choice = {0: 'r', 1: 'p', 2: 's'}

    choice = computer_choice[i]

    return choice

# Fix the error in this code!
# Given the user and computer input, this function
# determines who win
def won(user_input, computer_input):

    if user_input == 'r':
        if computer_input == 'p':
            return 'lost'
        elif computer_input == 's':
            return 'won'
        else:
            return 'draw'

    
    elif user_input == 'p':
        if computer_input == 'r':
            return 'won'
        elif computer_input == 's':
            return 'lost'
        else:
            return 'draw'

    else:
        if computer_input == 'r':
            return 'lost'
        
        elif computer_input == 'p':
            return 'won'
        else:
            return 'draw'

def print_win_message():
    print("Congratulations! You Beat the Computer!\n\n")

def print_lose_message():
    print("Sorry, you did not beat the computer\n\n")

def main():
    results = {'won': 1, 'lost': 0, 'draw': 0}
    letters_to_words = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'q': 'Quit'}
    finished = False

    while not finished:

        # get valid user input
        user_input = get_user_input()
        if user_input == 'q':
            break
        
        # get computer input
        ci = random.randint(0, 2)
        computer_input = get_computer_input(ci)

        # get results
        verdict = won(user_input, computer_input)
        print(f'You chose {letters_to_words[user_input]}, and the Computer chose {letters_to_words[computer_input]}')
        # checking to see if the player won or not
        if results[verdict] > 0:
            finished = True
            print_win_message()
        else:
            print_lose_message()

main()
