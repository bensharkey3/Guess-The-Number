import random

name = input('Enter your name:  ')

playing = 'y'

while playing == 'y':
    answer = random.randint(1,100)
    print('')
    print('Ok', name)
    guess = int(input('Guess a number between 1 and 100:  '))

    count = 1

    while guess != answer:
        if guess > answer:
            print('lower!')
        elif guess < answer:
            print('higher!')
        guess = int(input('guess again:  '))
        count += 1

    print('you got it!')
    print('it took you', count, 'guesses')
    print('')
    play_again = str(input('Play again? (enter y or n):  '))
    if play_again == 'n':
        input('Thanks for playing!')
        playing = 'n'
    elif play_again =='y':
        playing = 'y'
    else:
        print('invalid response, please enter y or n')
        play_again = str(input('Play again? (enter y or n):  '))
