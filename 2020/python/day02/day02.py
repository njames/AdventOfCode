import re
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # read in the input file as a list of ints
    data = [line for line in open('input.txt').read().strip().split('\n')]

    # print(data)
    correct_policies = 0
    correct_policies_part2 = 0
    t = time.perf_counter()
    for line in data:
        match = re.search('(\d*)-(\d*)\s([a-z]):\s([a-z]*)', line)
        # handy debugging to check my regex matched
        # I tested this at regext101.com
        # print(line)
        # print(match.group(1))
        # print(match.group(2))
        # print(match.group(3))
        # print(match.group(4))
        # exit(0)

        if int(match.group(1)) <= int(match.group(4).count(match.group(3))) <= int(match.group(2)):
            correct_policies += 1

        if (match.group(4)[int(match.group(1)) - 1] == match.group(3)) ^ \
                (match.group(4)[int(match.group(2)) - 1] == match.group(3)):
            correct_policies_part2 += 1

    print(f'Part 1: The number of correct policies is {correct_policies}')
    print(f'Part 2: The number of correct policies is {correct_policies_part2}')
    print(f'Time taken {time.perf_counter() - t} seconds')

    # part two
