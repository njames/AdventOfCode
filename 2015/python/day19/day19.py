import time
import re
import json

def replace_nth(string, sub, replace, n):
    find = string.find(sub)
    i = find != -1
    while find != -1 and i != n:
        find = string.find(sub, find + 1)
        i += 1
    if i == n:
        return string[:find] + replace + string[find + len(sub):]
    return string

def reverse_molecule(string, )


if __name__ == '__main__':
    # get input
    # with open('../../input/day19/input.txt', 'r') as file:
    with open('../../input/day19/input-test01.txt', 'r') as file:
        replacements = re.findall(r'(\w+) => (\w+)', file.read())
        file.seek(0)
        molecule = file.readlines()[-1]


    # part one
    valid = set()
    for x, y in replacements:
        count = molecule.count(x)
        for i in range(1, count + 1):
            new = replace_nth(molecule, x, y, i)
            valid.add(new)

    print(len(valid))
    print(replacements)

