import re
import time

def count_groups(data):

    result = [0, 0]
    groups = []
    counts = []
    tempGroup = set()
    groupCounter = 0
    for line in data:
        if len(line) == 0:
            groups.append(tempGroup.copy())
            counts.append(len(tempGroup))
            groupCounter += 1
            tempGroup.clear()

        for char in line:
            tempGroup.add(char)

    print('hey')
    print(groups)
    print('there')
    result[0] = sum(counts)

    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # read in the input file as a list of strings
    data = [line for line in open('../../input/day06/input.txt').read().split('\n')]
    # data = [line for line in open('../../input/day06/input-test01.txt').read().split('\n')]
    # data = [line for line in open('../../input/day05/input-test02.txt').read().strip().split('\n')]

    print(data)
    # for line in data:
    #     print(line)
    # exit(0)

    # test data
    t = time.perf_counter()

    groups = count_groups(data)

    # assert groups[0] == 11 # test01 data result
    # assert seats[1] == 820 # test02 data result

    print(f'Part 1: The total groups is {groups[0]}')

    # valid_pp = validate_data(data)
    # assert valid_pp[1] == 4 # test data result
    # print(f'Part 2: The seat is {seats[1]}')
    print(f'Time taken {time.perf_counter() - t} seconds')
