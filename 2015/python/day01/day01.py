import time
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # get input
    data = open('input.txt').read()

    t = time.perf_counter()
    # part one
    up = data.count('(')
    down = data.count(')')

    print(f"The floor is {up - down}")


    # part two
    floor = 0
    position = 0
    for c in data:
        position += 1
        floor = floor + 1 if c == '(' else floor - 1
        if floor == -1:
            print(f'Entered that basement at position {position}')
            print(f'Time taken {time.perf_counter() - t} seconds')
            exit(0)

