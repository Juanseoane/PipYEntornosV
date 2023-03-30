import random

options = ('rock', 'paper', 'scissors')

def main():
    rounds = input('How many rounds do you want to play? ')
    if rounds.isnumeric(): rounds = int(rounds)  
    else:
        print('You must insert a number')
        main()
    print(game(rounds))


def game(rounds):
    user_points = 0
    computer_points = 0
    round = 0
    while round != rounds:
        round += 1
        print(f'\nROUND {round}\n'+'*'*10)
        hand = input('CHOOSE: rock, paper or scissors => ').lower()
        computer = random.choice(options) # computer = options[random.randint(0,2)]
        if hand not in options:
            print("That's not a valid option => TRY AGAIN")
            round -= 1
        else:
            print(f"The computer's choice was {computer}")
            if hand == computer: 
                print('Even')
            elif (hand == 'rock' and computer == 'scissors') or (hand == 'paper' and computer == 'rock') or (hand == 'scissors' and computer == 'paper'):
                user_points += 1
                print('You won this round :)')
            elif (hand == 'rock' and computer == 'paper') or (hand == 'paper' and computer == 'scissors') or (hand == 'scissors' and computer == 'rock'):
                computer_points += 1
                print('You lost this round :(')
        print(f'------\nPOINTS\n------\nUser: {user_points}\nComputer: {computer_points}')
    return f'\n{"YOU WON THE GAME" if user_points > computer_points else "EVEN GAME" if user_points == computer_points else "YOU LOST THE GAME"}'

if __name__ == '__main__':
    print('///     WELCOME TO THE GAME     ///\n///              OF             ///\n///    ROCK, PAPER, SCISSORS    ///\n \n')
    main()