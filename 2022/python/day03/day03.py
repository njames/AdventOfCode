import time
from typing import List, Any


# Press the green button in the gutter to run the script.
def score(c):
    value = ord(c) - 96
    if value < 0:
        value = ord(c) - ord('A') + 27
    return value


def common(rucksacks):
    return list(filter(lambda x: x in rucksacks[0], rucksacks[1]))[0]


def splitLine(line=None):
    return [line[0:int(len(line) / 2)], line[int(len(line) / 2):]]


if __name__ == '__main__':
    # get input
    # data = [score(common(splitLine(line))) for line in open('../../input/day03/test.txt').read().strip().split('\n')]
    data = [score(common(splitLine(line))) for line in open('../../input/day03/input03.txt').read().strip().split('\n')]

    print('\n')
    print('Part 1', sum(data))

    t = time.perf_counter()
    # part one
    # print( ' Part 1 ', max(sums))

    # part two
    # sums.sort(reverse=True)
    # print('Part 2 ', sum(sums[0:3]))
