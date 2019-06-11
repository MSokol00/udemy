def reverse_string(item):
    return item[::-1]


def list_check(item):
    return all([type(i) == list for i in item])


def remove_every_other(item):
    return item[::2]


def sum_pairs(numbers, i):
    already_visited = set()
    for num in numbers:
        diff = i - num
        if diff in already_visited:
            return [diff, i]
        already_visited.add(num)
    return []


def vowel_count(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}


if __name__ == '__main__':
    print(reverse_string('awesome'))
    print(list_check([[], [1], [2, 3], [1, 2]]))
    print(remove_every_other([1, 2, 3, 4, 5]))
    print(sum_pairs([2, 4, 7, 5, 1], 6))
    print(vowel_count('awesome job my friend boss'))
