import random
import pandas as pd

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
    
    #df = pd.DataFrame(columns=['Date', 'Name', 'NumberOfGuesses'])
    #df.to_csv('GuessTheNumberGame.csv', index=False)
    '''only required to create a new csv'''
    
    df = pd.read_csv('GuessTheNumberGame.csv')
    df2 = pd.DataFrame([[pd.to_datetime('today'), name, count]], columns=['Date', 'Name', 'NumberOfGuesses'])
    df = df.append(df2)
    df.to_csv('GuessTheNumberGame.csv', index=False)
    
    play_again = str(input('Play again? (enter y or n):  '))
    if play_again == 'n':
        input('Thanks for playing!')
        playing = 'n'
    elif play_again =='y':
        playing = 'y'
    else:
        print('invalid response, please enter y or n')
        play_again = str(input('Play again? (enter y or n):  '))
