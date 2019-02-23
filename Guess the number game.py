import random
import pandas as pd

def verify_guess(i):
    '''validates guess to make sure its a number bertween 1-100'''
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
    
    '''only required to create a new csv'''
    #df = pd.DataFrame(columns=['Date', 'Name', 'NumberOfGuesses'])
    #df.to_csv('GuessTheNumberGame.csv', index=False)
    
    '''user stats'''
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
        input('Thanks for playing! - press enter to exit')
        playing = 'n'
    elif play_again =='y':
        playing = 'y'
    else:
        print('invalid response, please enter y or n')
        play_again = str(input('Play again? (enter y or n):  '))

# to do:
# guess charts and stats
# if csv file doesnt exist create a new one in pwd