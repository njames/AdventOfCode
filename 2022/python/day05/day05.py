import time
import re
from collections import deque

# piles data
#         [Q] [B]         [H]
#     [F] [W] [D] [Q]     [S]
#     [D] [C] [N] [S] [G] [F]
#     [R] [D] [L] [C] [N] [Q]     [R]
# [V] [W] [L] [M] [P] [S] [M]     [M]
# [J] [B] [F] [P] [B] [B] [P] [F] [F]
# [B] [V] [G] [J] [N] [D] [B] [L] [V]
# [D] [P] [R] [W] [H] [R] [Z] [W] [S]
#  1   2   3   4   5   6   7   8   9

piles = [deque(''),
         deque('DBJV'),
         deque('PVBWRDF'),
         deque('RGFLDCWQ'),
         deque('WJPMLNDB'),
         deque('HNBPCSQ'),
         deque('RDBSNG'),
         deque('ZBPMQFSH'),
         deque('WLF'),
         deque('SVFMR')
         ]

# test data
# piles = [deque(),
#          deque(['Z', 'N']),
#          deque(['M', 'C', 'D']),
#          deque(['P'])
#          ]

from typing import List, Any


# Press the green button in the gutter to run the script.

# currently taking the cheats way and manually contructing the input
def move(num, fr, to):
    for n in range(0, num):
        piles[to].append(piles[fr].pop())
    print(piles)


if __name__ == '__main__':
    # get input

    #    [D]
    # [N][C]
    # [Z][M][P]
    #  1  2  3

    # data = [line for line in open('../../input/day05/test.txt').read().strip().split('\n')]
    data = [line for line in open('../../input/day05/input05.txt').read().strip().split('\n')]

    # print('part 2 ',sum(scores2))

    for line in data:
        pattern = '\D*(\d*)\D*(\d*)\D*(\d*)'
        match = re.search(pattern, line)
        # print('match ', match.group(1), match.group(2), match.group(3)) // part 1
        a, b, c = int(match.group(1)), int(match.group(2)), int(match.group(3))
        move(a, b, 0) # move via 0 for part 2
        move(a, 0, c)

    print('\n\n')
    for l in range(1, len(piles)):
        print(piles[l][-1], end="")

    # print(piles)
    # print('\n')
    # print(data)

    # move(1, 2, 1)

    t = time.perf_counter()
    # part one
    # print( ' Part 1 ', max(sums))

    # part two
    # sums.sort(reverse=True)
    # print('Part 2 ', sum(sums[0:3]))
