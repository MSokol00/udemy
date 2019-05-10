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
        content = response.text
        print(f'Scraping posts data from: {url}...')
        soup = BeautifulSoup(content, 'html.parser')
        if soup.find('p', attrs={'class': 'lead'}).text.strip() == 'No matches found':
            break
        articles = soup.find_all("article")
        for article in articles:
            link = article.find("a")['href']
            title = article.find("a").text.strip()
            date = article.find("time")['datetime']
            writer.writerow({'title': title,
                             'link': link,
                             'date': date
                             })
        print(f'Scraped from {url} successful.')
        url = f'https://www.rithmschool.com/blog?page={i}'
        i += 1
