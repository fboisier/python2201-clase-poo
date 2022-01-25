# importa
import urllib.request
response = urllib.request.urlopen("https://www.breakingbadapi.com/api/characters/1")
html = response.read()
print(html)