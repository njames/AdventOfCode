import re
import time


def paper(l, w, h):
    a = l * w
    b = w * h
    c = h * l

    return 2 * (a + b + c) + min(a, b, c)


def ribbon(l, w, h):
    a = l + w
    b = w + h
    c = h + l

    return (l * w * h) + (2 * min(a, b, c))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # read in the input file as a list of ints
    data = [line for line in open('input.txt').read().strip().split('\n')]
    # data = ['2x3x4']
    # data = ['1x1x10']
    # print(data)
    wrapping = 0
    length_ribbon = 0
    # correct_policies_part2 = 0
    t = time.perf_counter()
    for line in data:
        match = re.search('(\d*)x(\d*)x(\d*)', line)
        wrapping += paper(int(match.group(1)), int(match.group(2)), int(match.group(3)))
        length_ribbon += ribbon(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    # assert wrapping == 58
    # assert wrapping == 43
    # assert length_ribbon == 34
    # assert length_ribbon == 14

    print(f'Part 1: The number of square feet required is {wrapping}')
    print(f'Part 2: The length of ribbon is {length_ribbon}')
    print(f'Time taken {time.perf_counter() - t} seconds')
    # 1606483
    # # part two
