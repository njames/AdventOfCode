import re
import time


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
    data = [line for line in open('../../input/day05/input05-test.txt').read().strip().split('\n')]
    # data = [line for line in open('../../input/day05/input05.txt').read().strip().split('\n')]
    # data = [line for line in open('../../input/day05/input-test02.txt').read().strip().split('\n')]

    print(data)

    points = []

    for line in data:
        match = re.findall('(\d)*,(\d)*', line)
        if match[0][0] == match[1][0] or match[0][1] == match[1][1]:
            points.append(match)

    # points now has only vertical and horizontal data

    print(points)


    # test data
    t = time.perf_counter()

    # seats = find_seat(data)
    # assert seats[0] == 820 # test01 data result
    # # assert seats[1] == 820 # test02 data result
    #
    # print(f'Part 1: The seat number is {seats[0]}')
    #
    # # valid_pp = validate_data(data)
    # # assert valid_pp[1] == 4 # test data result
    # print(f'Part 2: The seat is {seats[1]}')
    # print(f'Time taken {time.perf_counter() - t} seconds')
