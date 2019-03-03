import urllib.request

code = 'https://raw.githubusercontent.com/bensharkey3/Guess-The-Number/master/sourcecode.py'
response = urllib.request.urlopen(code)
data = response.read()
exec(data)
