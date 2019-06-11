def titleize(item):
    words = item.split(' ')
    titleized_words = [w[0].upper()+w[1:] for w in words]
    return ' '.join(titleized_words).strip()


def find_factors(num):
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
    return result


def find_factors_comp(num):
    return [i for i in range(1, num+1) if num % i == 0]


def includes(collection, value, index = 0):
    if type(collection) == dict:
        return value in collection.values()
    elif type(collection) in [str, list]:
        return value in collection[index:]


def repeat(string, num):
    return string*num


def truncate(string, n):
    if n >= 3:
        if len(string) >= n:
            return string[:n-3]+'...'
        return string
    return 'Truncation must be at least 3 characters.'


if __name__ == '__main__':
    #print(titleize('oNLy cAPITALIZe fIRSt'))
    #print(find_factors(111))
    #print(find_factors_comp(111))
    #print(includes([1, 2, 3], 1, 2))
    #print(repeat('abc', 0))
    print(truncate("Yo",100))