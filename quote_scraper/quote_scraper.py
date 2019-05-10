import requests
from bs4 import BeautifulSoup
from random import choice
from termcolor import cprint


class Quote:
    def __init__(self, author, quote, about_url):
        self.author = author
        self.quote = quote
        self._about_url = about_url
        self.about_author = {}

    def get_about_author(self) -> bool:
        response = requests.get(self._about_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        birth_date = soup.find('span', attrs={'class': 'author-born-date'}).text
        birth_place = soup.find('span', attrs={'class': 'author-born-location'}).text
        about = soup.find('div', attrs={'class': 'author-description'}).text.split('.')[0].replace(self.author,
                                                                                                   'AUTHOR').strip()
        self.about_author = {'birth': f'{birth_date} {birth_place}', 'about': about}
        return True


class Game:
    url = 'http://quotes.toscrape.com'

    def __init__(self):
        self.quotes = Game.scrape_quotes(Game.url)
        self.tries = 4
        self.random_quote = None
        self.about_author = {}

    @staticmethod
    def scrape_quotes(url: str) -> list:
        quotes_list = []
        next_url = url
        cprint(f'{"="*20}Start of Scraping{"="*20}', color='grey', on_color='on_white')
        i = 1
        while True:
            print(f'Scraping quotes from {next_url}...')
            response = requests.get(next_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = soup.find_all('div', attrs={'class': 'quote'})
            for quote in quotes:
                text = quote.find('span', attrs={'class': 'text'}).text
                author = quote.find('small', attrs={'class': 'author'}).text
                about_url = quote.find('a')['href']
                quotes_list.append(Quote(author=author, quote=text, about_url=f'{Game.url}{about_url}'))
            print('Scraping successful')
            if not soup.find('li', attrs={'class': 'next'}):
                cprint(f'{"="*30}Rnd of scraping{"="*30}', color='grey', on_color='on_white')
                break
            i += 1
            next_url = f'{url}/page/{i}/'
        return quotes_list

    def ask(self, quote: bool) -> bool:
        if quote:
            print(f'Here\' a quote:'
                  f'\n')
            cprint(f'\n{self.random_quote.quote}', color='magenta')
        answer = input(f'\nWho said this? Guesses remaining: {self.tries}.')
        if answer == self.random_quote.author:
            return True
        self.tries -= 1
        return False

    def give_hint(self):
        print('Here\'s a hint:')
        if self.tries == 3:
            cprint(f'The author first name starts with {self.random_quote.author[0]}, '
                   f'last name starts with {self.random_quote.author.split(" ")[1][0]}.', color='green')
        if self.tries == 2:
            self.random_quote.get_about_author()
            cprint(f'Author was born in {self.random_quote.about_author["birth"]}', color='green')
        if self.tries == 1:
            cprint(self.random_quote.about_author['about'], color='green')

    def play_game(self):
        count = 1
        while True:
            cprint(f'{"="*30}Start of Game {count}{"="*30}', color='grey', on_color='on_white')
            quote_print = True
            self.random_quote = choice(self.quotes)
            self.tries = 4
            while True:
                answer = self.ask(quote=quote_print)
                if answer:
                    print('You guessed correctly! Congratulations!')
                    break
                else:
                    if self.tries > 0:
                        self.give_hint()
                        quote_print = False
                    else:
                        print(f'Sorry, you\'ve run out of guesses. The answer was {self.random_quote.author}.')
                        break
            again = input('Do You like to play again (y/n)?')
            if again.lower().strip() == 'y':
                self.quotes.remove(self.random_quote)
                cprint(f'{"="*30}End of Game {count}{"="*30}', color='grey', on_color='on_white')
                count += 1
                continue
            cprint(f'{"="*30}End of Game - Terminating{"="*30}', color='grey', on_color='on_white')
            break


if __name__ == '__main__':
    game = Game()
    game.play_game()
