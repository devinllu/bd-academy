import random

def get_user_input():
    valid_inputs = ['r', 'p', 's', 'q']
    user_input = ''
    while user_input not in valid_inputs:
        user_input = input("Rock (r), Paper (p), Scissors (s), or Quit (q)?\n")


    return user_input

def get_computer_input(i):
    computer_choice = {0: 'r', 1: 'p', 2: 's'}

    choice = computer_choice[i]

    return choice

def won(user_input, computer_input):

    if user_input == 'r':
        if computer_input == 'p':
            return 'Lost'
        elif computer_input == 's':
            return 'Won'
        else:
            return 'Draw'

    
    elif user_input == 'p':
        if computer_input == 'r':
            return 'Won'
        elif computer_input == 's':
            return 'Lost'
        else:
            return 'Draw'

    else:
        if computer_input == 'r':
            return 'Lost'
        
        elif computer_input == 'p':
            return 'Won'
        else:
            return 'Draw'

def print_win_message():
    print("Congratulations! You Beat the Computer!")

def print_lose_message():
    print("Sorry, you did not beat the computer")

def main():
    results = {'Won': 1, 'Lost': 0, 'Draw': 0}
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
        print(f"You chose {letters_to_words[user_input]}, and the Computer chose {letters_to_words[computer_input]}")
        if results[verdict] > 0 :
            finished = True
            print_win_message()
        else:
            print_lose_message()

main()