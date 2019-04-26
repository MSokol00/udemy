import requests
from termcolor import cprint
from pyfiglet import Figlet
from random import choice

url = "https://icanhazdadjoke.com/search"
f = Figlet()
cprint(f.renderText('Dad Joke 3000'), color='red')
while True:
    topic = input('Let me tell You a joke! Give me a topic:')
    if len(topic):
        break
    cprint('Come on! What do You want to hear joke about?', color='red')

response = requests.get(
    url,
    headers={'Accept': 'application/json'},
    params={'term': topic},
)
data = response.json()
if not len(data['results']):
    print(f'Unfortunately there are no jokes about "{topic}" :(')
    exit(0)

print(f"I've got {len(data['results'])} about {topic}. Here's one:\n {choice(data['results'])['joke']}")
