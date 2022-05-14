import requests
from bs4 import BeautifulSoup
import bs4
import time

import json,io
import random

url = "https://type.fit/api/quotes"

#response = requests.get(url)
#response = response.json()
#soup = BeautifulSoup(response.content, "html.parser")
with open('study_quote_motivation.json', encoding='utf-8') as f1:
    study_quote = json.load(f1)

random_quote = random.choice(study_quote)
print('''
``{}``
---{}---
'''.format(random_quote["text"],random_quote["author"]))

