

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    target = 2020

    # read in the input file as a list of ints
    expenses = [int(x) for x in open('input.txt').read().strip().split('\n')]

    for x in expenses:
        find = target - x
        if find in expenses:
            print(find * x)
            exit(0)




