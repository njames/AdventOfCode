import re
import time





# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # read in the input file as a list of ints
    data = [line for line in open('input.txt').read().strip().split('\n')]
    t = time.perf_counter()
    # first thoughts
    # get the length of the line and treat this as a modular arithmetic to wrap around when counting to the right
    trees = 0
    cols = len(data[0])
    rows = len(data)
    r = c = 0
    while r < rows:
        if data[r][c] == '#':
            trees += 1
        r += 1
        c = (c + 3) % cols




    # print(f'line len {length} rows {rows}')
    # print(data)

    print(f'Part 1: The number of trees encountered  is {trees}')
    print(f'Part 2: The number of correct policies is {0}')
    print(f'Time taken {time.perf_counter() - t} seconds')

    # part two
