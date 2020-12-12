import re
import time


def change_direction(degrees, lr, current):
    rotate = int(degrees / 90)
    new = current.copy()
    for i in range(rotate):
        if lr == 'R':
            new[0], new[1] = new[1], new[0] * -1
        else:
            new[0], new[1] = new[1] * -1, new[0]

    return new


def manhattan(pos):
    return abs(pos[0]) + abs(pos[1])


def calc_manhattan(data):
    current_direction = [1, 0]
    position = [0, 0]

    direction_vectors = {'E': (1, 0),
                         'N': (0, 1),
                         'W': (-1, 0),
                         'S': (0, -1)
                         }

    for instruction in data:
        move = instruction[0]
        length = int(instruction[1:])
        if move == 'L' or move == 'R':
            current_direction = change_direction(length, move, current_direction)
        elif move == 'F':
            # print(f'Direction {current_direction}')
            position[0] += current_direction[0] * length
            position[1] += current_direction[1] * length
        else:
            position[0] += direction_vectors[move][0] * length
            position[1] += direction_vectors[move][1] * length

        # print(position)

    return manhattan(position)


def calc_manhattan_waypoint(data):
    current_direction = [10, 1]
    position = [0, 0]

    direction_vectors = {'E': (1, 0),
                         'N': (0, 1),
                         'W': (-1, 0),
                         'S': (0, -1)
                         }

    print(f'direction {current_direction} position {position}')

    for instruction in data:
        print(instruction)
        move = instruction[0]
        length = int(instruction[1:])
        if move == 'L' or move == 'R':
            current_direction = change_direction(length, move, current_direction)
        elif move == 'F':
            print(f'Direction {current_direction}')
            position[0] += current_direction[0] * length
            position[1] += current_direction[1] * length
        else:
            current_direction[0] += (direction_vectors[move][0] * length) #* current_direction[0]
            current_direction[1] += (direction_vectors[move][1] * length) #* current_direction[1]

        print(f'direction {current_direction} position {position}')

    return manhattan(position)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # read in the input file as a list strings
    data = [line for line in open('../../input/day12/input.txt').read().strip().split('\n')]
    # data = [line for line in open('../../input/day12/input-test01.txt').read().strip().split('\n')]

    # for line in open('../../input/day12/input-test02.txt').read().strip().split('\n\n')]

    # for line in data:
    #     print(line)

    # exit(0)

    # test data
    t = time.perf_counter()

    distance = calc_manhattan(data)


    print(f'Part 1: The manhattan distance is {distance}')

    distance = calc_manhattan_waypoint(data)

    print(f'Part 2: The manhattan distance is {distance}')
    print(f'Time taken {time.perf_counter() - t} seconds')
