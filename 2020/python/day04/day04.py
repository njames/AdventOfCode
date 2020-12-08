import re
import time


def validate_passports(data):
    passports = [0, 0]
    for line in data:
        if 'byr' in line and \
                'iyr' in line and \
                'eyr' in line and \
                'hgt' in line and \
                'hcl' in line and \
                'ecl' in line and \
                'pid' in line:
            # 'cid' in line and \
            passports[0] += 1
        else:
            continue

    #     part two
        if not 1920 <= int(line['byr']) <= 2002:
            continue
        if not 2010 <= int(line['iyr']) <= 2020:
            continue
        if not 2020 <= int(line['eyr']) <= 2030:
            continue
        if line['hgt'].endswith('cm'):
            if not 150 <= int(line['hgt'][:-2]) <= 193:
                continue
        elif line['hgt'].endswith('in'):
            if not 59 <= int(line['hgt'][:-2]) <= 76:
                continue
        else:
            continue
        if not re.fullmatch(r'#[0-9a-f]{6}', line['hcl']):
            continue
        if line['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue
        if not re.fullmatch(r'[0-9]{9}', line['pid']):
            continue

        passports[1] += 1

    return passports

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # read in the input file as a list of key value pairs aka python dictionary
    data = [{
        (key := l.split(":"))[0]: key[1]
        for l in line.replace("\n", " ").strip().split(" ")
    }
    for line in open('../../input/day04/input.txt').read().strip().split('\n\n')]
    # for line in open('../../input/day04/input-test01.txt').read().strip().split('\n\n')]
    # for line in open('../../input/day04/input-test02.txt').read().strip().split('\n\n')]

    # for line in data:
    #     print(line)
    #
    # exit(0)

    # test data
    t = time.perf_counter()

    valid_pp = validate_passports(data)
    # assert valid_pp == 2 # test data result


    print(f'Part 1: The number of valid passports is {valid_pp[0]}')

    # valid_pp = validate_data(data)
    # assert valid_pp[1] == 4 # test data result
    print(f'Part 2: The number of valid passports is {valid_pp[1]}')
    print(f'Time taken {time.perf_counter() - t} seconds')
