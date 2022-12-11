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


def commonSet(r1, r2):
    return set(filter(lambda x: x in r1, r2))


def splitLine(line=None):
    return [line[0:int(len(line) / 2)], line[int(len(line) / 2):]]


if __name__ == '__main__':
    # get input
    # data = [line for line in open('../../input/day03/test.txt').read().strip().split('\n')]
    data = [line for line in open('../../input/day03/input03.txt').read().strip().split('\n')]

    part1 = []
    for line in data:
        part1.append(score(common(splitLine(line))))

    print('\n')
    print('Part 1', sum(part1))

    part2 = []

    for i in range(0, len(data), 3):
        part2.append(score(commonSet(data[i], data[1 + i]).intersection(commonSet(data[1 + i], data[2 + i])).pop()))

    print('Part 2', sum(part2))

    t = time.perf_counter()
