from termcolor import cprint
from pyfiglet import Figlet


def ascii_art():
    colors = ['grey', 'red', 'green', 'yellow',
              'blue', 'magenta', 'cyan', 'white']
    text = input('What message do You want to print?')
    colorsText = 'In what color? (select number):'+'\n'.join(
        f'{n}-{value}'for n, value in enumerate(colors, 1))
    while True:
        try:
            n = int(input(colorsText))
            if n > len(colors):
                cprint("Select value from the list", color='red')
                continue
            break
        except (TypeError, ValueError):
            cprint('Nice Try! Pick a number.', color='red')
    f = Figlet(font='slant')
    cprint(f.renderText(text), color=colors[n-1])


if __name__ == '__main__':
    ascii_art()
