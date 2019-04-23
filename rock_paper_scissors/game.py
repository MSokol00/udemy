from random import choice

ANSWERS = ['rock', 'paper', 'scissors']
RULES = [('rock', 'paper', 2),
         ('rock', 'scissors', 1),
         ('paper', 'scissors', 2),
         ('paper', 'rock', 1),
         ('scissors', 'rock', 2),
         ('scissors', 'paper', 1)]


def start():
    print("...rock...\n...paper...\n...scissors...")

    p1 = get_answer(1)
    p2 = choice(ANSWERS)
    print(f"Player 2's choice is: {p2}")

    win = evaluate(p1, p2)

    print('SHOOT!')
    if win == 0:
        print('DRAW!')
    else:
        print(f"Player{win} wins!")


def get_answer(player):
    answer = ''
    while answer == '':
        answer = input(f'Enter Player {player}\'s choice:')
        if answer not in ANSWERS:
            print(f'This is not correct answer, only following are valid: {ANSWERS}')
            answer = ''
    return answer


def evaluate(p1, p2):
    if p1 == p2:
        return 0
    else:
        for a, b, w in RULES:
            if a == p1 and b == p2:
                return w


if __name__ == '__main__':
    start()
