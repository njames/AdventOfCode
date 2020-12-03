import re
import time

def check_slope(data, slope):
    cols = len(data[0])
    rows = len(data)
    r = c = 0
    trees = 0
    while r < rows:
        if data[r][c] == '#':
            trees += 1
        r += slope[0]
        c = (c + slope[1]) % cols

    return trees

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # read in the input file as a list of ints
    data = [line for line in open('input.txt').read().strip().split('\n')]
    t = time.perf_counter()
    # first thoughts
    # get the length of the line and treat this as a modular arithmetic to wrap around when counting to the right
    trees = check_slope(data, [1, 3])
    print(f'Part 1: The number of trees encountered  is {trees}')

    trees = 1

    slopes = [
        [1, 1],
        [1, 3],
        [1, 5],
        [1, 7],
        [2, 1],
    ]

    for slope in slopes:
        trees *= check_slope(data, slope)

    # print(f'line len {length} rows {rows}')
    # print(data)

    print(f'Part 2: The number of multiplied trees is {trees}')
    print(f'Time taken {time.perf_counter() - t} seconds')

    # part two
