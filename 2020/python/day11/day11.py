import re
import time
import numpy as np


def check_seats(input_map, floor):
    dim_x = int(len(input_map[0]))
    dim_y = int(len(input_map))
    next_map = input_map.copy()

    while True:
        for y in range(dim_y):
            for x in range(dim_x):
                # calculate the sum of the square around x, y adjusting for boundaries
                sub_xl = max(x - 1, 0)
                sub_xu = min(x + 2, dim_x)
                sub_yl = max(y - 1, 0)
                sub_yu = min(y + 2, dim_y)

                sum_of_sub_square = sum(sum(input_map[sub_yl:sub_yu, sub_xl:sub_xu]))

                if floor[y][x] == '.':
                    continue

                if input_map[y][x] == 0 and sum_of_sub_square == 0:
                    next_map[y][x] = 1
                if input_map[y][x] == 1 and (sum_of_sub_square - 1) > 3:
                    next_map[y][x] = 0

        if (next_map == input_map).all():
            return next_map
        else:
            input_map = next_map.copy()


def check_seats_diagonal(input_map, floor):
    dim_x = int(len(input_map[0]))
    dim_y = int(len(input_map))
    next_map = input_map.copy()


    # create a set of tuples for the eight directions
    directions = [ (1,0), (1, 1), (0,1), (-1, 1),
                   (-1, 0), (-1, -1), (0, -1), (1, -1)
                   ]
    while True:
        for y in range(dim_y):
            for x in range(dim_x):

                seat_count = 0
                for d in directions:

                    found = False
                    while not found:
                        try_count = 1
                        try_x = x + (d[0] * try_count)
                        try_y = y + (d[1] * try_count)
                        if input_map[try_y][try_x] == 1:
                            found = True
                            seat_count += 1
                        if input_map[try_y][try_x] == 0 and floor[try_y][try_x] != '.':
                            found = True

        if (next_map == input_map).all():
            return next_map
        else:
            input_map = next_map.copy()

    return next_map

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # read in the input file as a list of strings
    # Transform occupied from # -> 1
    # Transform unoccupied from L -> 0
    # Transform floor  from . -> ' '
    # data = [line for line in
    #         open('../../input/day11/input.txt').read().strip().replace('L', '0').replace('#', '1').split('\n')]
    data = [line for line in
            open('../../input/day11/input-test01.txt').read().strip().replace('L', '0').replace('#', '1').split('\n')]
    # data = [line for line in open('../../input/day11/input-test02.txt').read().strip().split('\n')]

    t = time.perf_counter()
    int_data = np.empty([len(data), len(data[0])], dtype='float')
    next_data = int_data.copy()

    for y in range(len(data)):
        for x in range(len(data[0])):
            try:
                int_data[y][x] = int(data[y][x])
            except ValueError:
                int_data[y][x] = 0

    # print('input')
    # print(int_data)
    # print(data)


    occupied_seats = int(sum(sum(check_seats(int_data, data))))

    # test data

    # seats = find_seat(data)
    # assert seats[0] == 820 # test01 data result
    # assert seats[1] == 820 # test02 data result

    print(f'Part 1: The seat number is {occupied_seats}')

    # valid_pp = validate_data(data)
    # assert valid_pp[1] == 4 # test data result

    occupied_seats = int(sum(sum(check_seats_diagonal(int_data, data))))
    print(f'Part 2: The seat is {occupied_seats}')
    print(f'Time taken {time.perf_counter() - t} seconds')
