import time
from typing import List, Any


# Press the green button in the gutter to run the script.

def inside(x, y):
    return int(x[0]) <= int(y[0]) and int(x[1]) >= int(y[1])


def overlap(x, y):
    return int(x[0]) <= int(y[0]) <= int(x[1]) <= int(y[1])


if __name__ == '__main__':
    # get input
    # data = [line.split(',') for line in open('../../input/day04/test.txt').read().strip().split('\n')]
    data = [line.split(',') for line in open('../../input/day04/input04.txt').read().strip().split('\n')]

    assert inside([1, 10], [1, 10]) == True
    assert inside([1, 2], [3, 4]) == False

    insideData = []
    overlapData = []
    # print('part 1 ',sum(scores))
    for line in data:
        # print(line)
        a, b = line[0].split('-'), line[1].split('-')

        print(a, b)
        if inside(a, b) or inside(b, a):
            print('inside')
            insideData.append(1)

        if overlap(a, b) or overlap(b, a) or inside(a, b) or inside(b, a):
            print('overlap')
            overlapData.append(1)

    print('Part 1', sum(insideData))
    print('Part 2', sum(overlapData))

    # print('part 1 ',sum(scores2))

    # print('\n')
    # print(scores)

    t = time.perf_counter()
    # part one
    # print( ' Part 1 ', max(sums))

    # part two
    # sums.sort(reverse=True)
    # print('Part 2 ', sum(sums[0:3]))
