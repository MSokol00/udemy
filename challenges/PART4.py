def sum_up_diagonals(lists):
    sum = 0
    for i in range(len(lists)):
        sum += lists[i][i]
    for i in range(-len(lists), 0):
        sum += lists[i][i]
    return sum


def min_max_key_in_dictionary



if __name__ == '__main__':
    list4 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print(sum_up_diagonals(list4))