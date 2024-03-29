import time
from typing import List, Any

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    # get input
    # data = [line.split(' ') for line in open('../../input/day02/test.txt').read().strip().split('\n')]
    data = [line.split(' ') for line in open('../../input/day02/input02.txt').read().strip().split('\n')]

    scores: list[int] = []
    scores2: list[int] = []
    for game in data:
        o = ord(game[0]) - ord('A')
        m = ord(game[1]) - ord('X')

        # equal
        if o == m:
            scores.append(m + 1 + 3)
            print(o, m, 'draw')
        #     m wins
        elif ((o + 1) % 3) == m:
            scores.append(m + 1 + 6)
            print(o, m, 'win')
        else:
            scores.append(m + 1)
            print(o, m, 'loss')

    print('part 2 ',sum(scores))

    for game in data:
        o = ord(game[0]) - ord('A')
        m = ord(game[1]) - ord('X')

        if m == 0: # lose
            scores2.append(((o - 1) % 3) + 1)
        elif m == 1: # draw
            scores2.append(o + 1 + 3)
        else: # win
            scores2.append(((o + 1) % 3) + 1 + 6)

    print('part 2 ',sum(scores2))

    # print('\n')
    # print(scores)

    t = time.perf_counter()
    # part one
    # print( ' Part 1 ', max(sums))

    # part two
    # sums.sort(reverse=True)
    # print('Part 2 ', sum(sums[0:3]))
