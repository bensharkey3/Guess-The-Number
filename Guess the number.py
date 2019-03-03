import urllib.request

code = 'https://raw.githubusercontent.com/bensharkey3/Guess-The-Number/master/Guess%20the%20number%20game.py'
response = urllib.request.urlopen(code)
data = response.read()
exec(data)
