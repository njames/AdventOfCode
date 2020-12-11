import re
import time
import numpy as np


def find_seat(data):
    seats = []
    result = [0, 0]

    boarding_row = 0
    for row in data:
        boarding_row = int(row[:7].replace('B', '1').replace('F', '0'), 2)
        boarding_seat = int(row[-3:].replace('R', '1').replace('L', '0'), 2)
        seats.append(boarding_row * 8 + boarding_seat)

    result[0] = max(seats)
    print(seats)

    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # read in the input file as a list of strings
    # Transform occupied from # -> 1
    # Transform unoccupied from L -> 0
    # Transform floor  from . -> ' '
    # data = [line for line in open('../../input/day11/input.txt').read().strip().split('\n')]
    data = [line for line in open('../../input/day11/input-test01.txt').read().strip().replace('L', '0').replace('#', '1').replace('.', ' ').split('\n')]
    # data = [line for line in open('../../input/day11/input-test02.txt').read().strip().split('\n')]
    # intData

    intData = np.empty([len(data[0]), len(data)])

    for x in range(len(data)):
        for y in range(len(data[0])):
            try:
                intData[x][y] = int(data[x][y])
            except ValueError:
                intData[x][y] = None


    print(intData)


    # for line in data:
    #     print(line)
    exit(0)

    # test data
    t = time.perf_counter()

    seats = find_seat(data)
    # assert seats[0] == 820 # test01 data result
    # assert seats[1] == 820 # test02 data result

    print(f'Part 1: The seat number is {seats[0]}')

    # valid_pp = validate_data(data)
    # assert valid_pp[1] == 4 # test data result
    print(f'Part 2: The seat is {seats[1]}')
    print(f'Time taken {time.perf_counter() - t} seconds')
