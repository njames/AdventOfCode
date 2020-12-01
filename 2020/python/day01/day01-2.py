

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    target = 2020

    # read in the input file as a list of ints
    expenses = [int(x) for x in open('input.txt').read().strip().split('\n')]

    for i, item1 in enumerate(expenses):
        find1 = target - item1
        for j, item2 in enumerate(expenses[i+1:]):
            find2 = find1 - item2
            if find2 in expenses[j+1:]:
                print("{} + {} + {} = {}".format(item1, find2, item2, (item1 + find2 + item2)))
                print(item1 * find2 * item2)
                exit(0)




