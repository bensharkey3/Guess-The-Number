import random
import os
import pandas as pd

def verify_guess(i):
    '''validates a guess to make sure its a number between 1-100'''
    while True:
        try:
            i = int(i)
            if i>0 and i<101:
                return i
            else:
                raise
            break
        except:
            print('not a valid number!')
            i = input('Guess a number between 1 and 100:  ')

def user_stats():
    '''generates user stats'''
    try:
        csvfileloc = 'C:\\Users\\user\\Google Drive\\Guess-The-Number\\GuessTheNumberGameData.csv'
        df = pd.read_csv(csvfileloc)
    except:
        try:
            csvfileloc = '{}\\GuessTheNumberGameData.csv'.format(os.getcwd())
            df = pd.read_csv(csvfileloc)
        except:
            df = pd.DataFrame(columns=['Date', 'Name', 'NumberOfGuesses'])
            csvfileloc = '{}\\GuessTheNumberGameData.csv'.format(os.getcwd())
            df.to_csv(csvfileloc, index=False)

    df2 = pd.DataFrame([[pd.to_datetime('today'), name, count]], columns=['Date', 'Name', 'NumberOfGuesses'])
    df = df.append(df2)
    df.to_csv(csvfileloc, index=False)
    df = pd.read_csv(csvfileloc)
    df3 = df.groupby('Name').mean().sort_values(by='NumberOfGuesses').reset_index()
    df4 = df.groupby('Name')[['Date']].count()
    df5 = df.groupby('Name')[['NumberOfGuesses']].min()
    dfprint = df3.merge(df4, on='Name').merge(df5, on='Name')
    dfprint.rename(columns={'NumberOfGuesses_x':'Ave Number of Guesses', 'Date':'Games Played', 'NumberOfGuesses_y':'Best'}, inplace=True)
    dfprint['Ave Number of Guesses'] = dfprint['Ave Number of Guesses'].round(2)
    print(dfprint)


'''run the program'''
name = input('Enter your name:  ')

playing = 'y'

while playing == 'y':
    answer = random.randint(1,100)
    print('')
    print('Ok', name)
    guess = verify_guess(input('Guess a number between 1 and 100:  '))

    count = 1

    while guess != answer:
        if guess > answer:
            print('lower!')
        elif guess < answer:
            print('higher!')
        guess = verify_guess(input('guess again:  '))
        count += 1

    print('you got it!')
    print('it took you {} guesses'.format(count))
    print('')

    user_stats()

    while True:
        playagain = str(input('Play again? (enter y or n):  '))
        if playagain == 'n':
            input('Thanks for playing! - press enter to exit')
            playing = 'n'
            break
        elif playagain =='y':
            playing = 'y'
            break
        else:
            print('invalid response, please enter y or n')

# to do:
# chart user statistics
