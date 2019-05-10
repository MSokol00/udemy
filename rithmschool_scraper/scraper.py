from bs4 import BeautifulSoup
from csv import DictWriter
import requests

"""
grab links from rithm schol blog
Data: store URL, anchor tag text and date into CSV
"""

url = 'https://www.rithmschool.com/blog'
i = 2
with open('posts.csv', 'w') as file:
    f_names = ['title', 'link', 'date']
    writer = DictWriter(file, fieldnames=f_names)
    writer.writeheader()

    while True:
        response = requests.get(url)
        if response.status_code == 404:
            break
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        articles = soup.find_all("article")
        for article in articles:
            link = article.find("a")['href']
            title = article.find("a").text.strip()
            date = article.find("time")['datetime']
            writer.writerow({'title': title,
                             'link': link,
                             'date': date
                             })
        url = f'https://www.rithmschool.com/blog?page={i}'
        print(url)
        i += 1
