def two_list_dictionary(list1, list2):
    result = {}
    for i in range(len(list1)):
        try:
            result[list1[i]] = list2[i]
        except IndexError:
            result[list1[i]] = None
    return result


def range_in_list(list, start=0, end=None):
    if end == None or end > len(list):
        end = len(list)-1
    return sum(list[start:end+1])


def same_frequency(num1, num2):
    return all(str(num1).count(i) == str(num2).count(i) for i in str(num1))


def nth(list, num):
    return list[num]


def find_the_duplicate(array):
    result = [num for num in array if array.count(num) > 1]
    if result:
        return result[0]


if __name__ == '__main__':
    #print(two_list_dictionary(['x', 'y', 'z']  , [1,2]))
    #print(range_in_list([1,2,3,4],1))
    #print(same_frequency(1212, 2211))
    print(find_the_duplicate([2,1,3,4]))