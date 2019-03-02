import random
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

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
            i = input('guess a number between 1 and 100:  ')

def verify_num(i):
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
            i = input('Enter a number for the computer to guess:  ')
            
def stats():
    '''generates user stats'''
    try:
        csvfileloc = 'C:\\Users\\user\\Google Drive\\Guess-The-Number\\GuessTheNumberGameData.csv'
        df = pd.read_csv(csvfileloc)
    except:
        try:
            csvfileloc = '{}\\GuessTheNumberGameData.csv'.format(os.getcwd())
            df = pd.read_csv(csvfileloc)
        except:
            df = pd.read_csv('https://raw.githubusercontent.com/bensharkey3/Guess-The-Number/master/GuessTheNumberGameData.csv')
            csvfileloc = '{}\\GuessTheNumberGameData.csv'.format(os.getcwd())
            df.to_csv(csvfileloc, index=False)
    df2 = pd.DataFrame([[pd.to_datetime('today'), name, count, diff], [pd.to_datetime('today'), 'the computer', ccount, -diff]], columns=['Date', 'Name', 'NumberOfGuesses', 'DiffToOpponent'])
    df = df.append(df2)
    df.to_csv(csvfileloc, index=False)
    df = pd.read_csv(csvfileloc)
    df3 = df.groupby('Name').mean().sort_values(by='NumberOfGuesses').reset_index()
    df4 = df.groupby('Name')[['Date']].count()
    df5 = df.groupby('Name')[['NumberOfGuesses']].min()
    dfprint = df3.merge(df4, on='Name').merge(df5, on='Name')
    df6 = df[df['DiffToOpponent'].notnull()].groupby('Name').count()[['Date']]
    df6.rename(columns={'Date':'Played'}, inplace=True)
    df6['Lost'] = df[df['DiffToOpponent'] > 0].groupby('Name').count()['Date']
    df6['Won'] = df[df['DiffToOpponent'] < 0].groupby('Name').count()['Date']
    df6['Drew'] = df[df['DiffToOpponent'] == 0].groupby('Name').count()['Date']
    dfprint = dfprint.merge(df6, how='left', on='Name')
    dfprint.rename(columns={'NumberOfGuesses_x':'Average', 'Date':'Turns', 'NumberOfGuesses_y':'Best'}, inplace=True)
    dfprint['Average'] = dfprint['Average'].round(2)
    dfprint['W/L%'] = round(dfprint['Won']*100 / (dfprint['Lost'] + dfprint['Won']), 1)
    dfprint = dfprint[['Name', 'Average', 'Turns', 'Best', 'Played', 'Won', 'Lost', 'Drew', 'W/L%']]
    dfprint.fillna(value=0, inplace=True)
    print(dfprint)
    '''generates histogram'''
    plt.hist(df[(df['Name'] == name)]['NumberOfGuesses'], bins=(0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5), histtype='stepfilled', normed=True, color='b', alpha=0.3, label=name)
    plt.hist(df['NumberOfGuesses'], bins=(0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5), histtype='stepfilled', normed=True, color='r', alpha=0.3, label='all players', )
    plt.title("Number of Guesses")
    plt.legend(loc='upper left')
    plt.xticks([1,2,3,4,5,6,7,8,9])
    plt.ylabel("Frequency")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.show()


'''run the program'''
name = input('Enter your name:  ')

playing = 'y'

while playing == 'y':
    answer = random.randint(1,100)
    print(' ')
    print('ok', name)
    print(' ')
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
    print('you guessed it in {} guesses'.format(count))
    print(' ')
    input('press enter to see how you compared to the computer')
    print(' ')

    '''computers guesses'''
    low = 1
    high = 100
    ccount = 1
    cguess = random.choice([36, 64])
    while cguess != answer:
        print("the computer's guess {}:  {}".format(ccount, cguess))
        if cguess > answer:
            print('lower!')
        elif cguess < answer:
            print('higher!')
        if cguess > answer:
            high = cguess
        elif cguess < answer:
            low = cguess + 1
        cguess = (low+high)//2
        ccount += 1
    
    diff = count - ccount
    print("the computer's guess {}:  {}".format(ccount, cguess))
    print('got it!')
    print('The computer took {} guesses'.format(ccount))
    print(' ')
    if ccount > count:
        print(' - you defeated the computer by {} guess(es)!'.format(-diff))
        print(' ')
    elif count > ccount:
        print(' - the computer defeated you by {} guess(es)'.format(diff))
        print(' ')
    else:
        print(" - it's a draw!")
        print(' ')
    
    stats()

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
# histograam ticks in between number labels
# table index to start at 1
# table formatting
# chart % formatting zero decimals
# text result is returning incorrectly
# execute code directly from github