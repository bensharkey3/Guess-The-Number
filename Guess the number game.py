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
    
    csvfileloc = 'C:\\Users\\user\\Google Drive\\Guess-The-Number\\GuessTheNumberGameData.csv'
    df = pd.read_csv(csvfileloc)
    df2 = pd.DataFrame([[pd.to_datetime('today'), name, count]], columns=['Date', 'Name', 'NumberOfGuesses'])
    df = df.append(df2)
    df.to_csv(csvfileloc, index=False)
    df = pd.read_csv(csvfileloc)
    df3 = df.groupby('Name').mean().sort_values(by='NumberOfGuesses').reset_index()
    df4 = df.groupby('Name')[['Date']].count()
    df5 = df.groupby('Name')[['NumberOfGuesses']].min()
    dfprint = df3.merge(df4, on='Name').merge(df5, on='Name')
    dfprint.rename(columns={'NumberOfGuesses_x':'Ave Number of Guesses', 'Date':'Games Played', 'NumberOfGuesses_y':'Best'}, inplace=True)
    print(dfprint)
    
    play_again = str(input('Play again? (enter y or n):  '))
    if play_again == 'n':
        input('Thanks for playing!')
        playing = 'n'
    elif play_again =='y':
        playing = 'y'
    else:
        print('invalid response, please enter y or n')
        play_again = str(input('Play again? (enter y or n):  '))

# to do
# answer verification
# guess charts
