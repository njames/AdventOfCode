import time
from collections import deque
from typing import List, Any

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    # get input
    # data = open('../../input/day06/test.txt').read()
    data = open('../../input/day06/input06.txt').read()

    print(data)
    print(len(data))
    result = 0
    # marker_length = 4 # part 1
    marker_length = 14
    max = len(data) - marker_length
    count = 0
    list = deque('', maxlen=marker_length)

    while count < max and result < 1:
        list.append(data[count])
        if count >= marker_length and len(set(list)) == marker_length:
            result = count + 1

        count += 1

    print('Part 1: ', result)
    # print('\n')
    # print(scores)

    t = time.perf_counter()
    # part one
    # print( ' Part 1 ', max(sums))

    # part two
    # sums.sort(reverse=True)
    # print('Part 2 ', sum(sums[0:3]))
