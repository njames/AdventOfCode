import time
# Press the green button in the gutter to run the script.



if __name__ == '__main__':
    # get input
    # data = [line for line in open('../../input/day01/test.txt').read().strip().split('\n\n')]
    data = [line for line in open('../../input/day01/input01.txt').read().strip().split('\n\n')]
    sums = []
    for line in data:
        intLine = [ int(x) for x in line.split('\n')]
        sums.append(sum(intLine))


    t = time.perf_counter()
    # part one
    print( ' Part 1 ', max(sums))


    # part two
    sums.sort(reverse=True)
    print('Part 2 ', sum(sums[0:3]))

