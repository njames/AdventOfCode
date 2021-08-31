import re
import time
import numpy as np

#  globals
fields = {}
my_ticket = []
nearby_tickets = []
row_count = -1
my_row = 1000000

invalid_tickets = []


def is_valid(ticket):
    global fields
    valid = True
    #     check all values in the ticket to see if they are in valid ranges
    for field in fields:
        for t in ticket:
            
            valid = (field[0][0] < t < field[0][1] ) or \
                (field[1][0] < t < field[1][1])
    return valid


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # input is a set of rules

    # details of my seat

    # details of nearby seats




    # read in the input file as a list of strings
    # data = [line for line in
    #         open('../../input/day11/input.txt').read().strip().replace('L', '0').replace('#', '1').split('\n')]
    # data = [line for line in
            # open('../../input/day16/input-test01.txt').read().strip().split('\n')]

        data = [line for line in open('../../input/day16/input.txt').read().strip().split('\n')]

    # fields = {'class' : [0, 3], [9, 10]} <- get data in this shape

    for row in data:
        row_count += 1
        match = re.search('([\w +]+): (\d*)-(\d*) or (\d*)-(\d*)', row)
        if match:
            fields[match.group(1)] = [[int(match.group(2)), int(match.group(3))] ,[int(match.group(4)), int(match.group(5))]]
            continue

        #  get my ticket
        match = re.search('your ticket:', row)

        if match:
            print(row)
            my_row = row_count + 1
            my_ticket = [int(d) for d in data[my_row].strip().split(',')]
            continue

        #
        match = re.search('nearby tickets:', row)
        if match:
            my_row = row_count
            print(row)
            continue

        if row_count >  my_row and row != '':
            nearby_tickets.append([int(d) for d in data[row_count].strip().split(',')])
        # get remaining tickets



        # if row.split(':'):
        #     row.
    # t = time.perf_counter()
    # int_data = np.empty([len(data), len(data[0])], dtype='float')
    # next_data = int_data.copy()

    # for y in range(len(data)):
    #     for x in range(len(data[0])):
    #         try:
    #             int_data[y][x] = int(data[y][x])
    #         except ValueError:
    #             int_data[y][x] = 0

    # print('input')
    # print(int_data)
    # print(fields)
    # print(my_ticket)
    # print(nearby_tickets)

    for f in fields:
        print(f)

    for t in nearby_tickets:
        if not is_valid(t):
            invalid_tickets.append(t)




    # test data

    # seats = find_seat(data)
    # assert seats[0] == 820 # test01 data result
    # assert seats[1] == 820 # test02 data result

    # print(f'Part 1: The seat number is {occupied_seats}')

    # valid_pp = validate_data(data)
    # assert valid_pp[1] == 4 # test data result

    # occupied_seats = int(sum(sum(check_seats_diagonal(int_data, data))))
    # print(f'Part 2: The seat is {occupied_seats}')
    # print(f'Time taken {time.perf_counter() - t} seconds')
