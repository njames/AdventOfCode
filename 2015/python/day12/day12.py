import time
import re
import json

# this isnt working right now
def walk(d):
    global path, sum

    if isinstance(d, dict):
        for k, v in d.items():
            if isinstance(v, int):
                path.append(k)
                sum = sum + int(v)
                path.pop()
            elif v is None:
                path.append(k)
                ## do something special
                path.pop()
            elif isinstance(v, dict):
                path.append(k)
                walk(v)
                path.pop()
    elif isinstance(d, list):
        
    return sum


if __name__ == '__main__':
    # get input
    file = open('../../input/day12/input.json').read()
    data = json.dumps(file)

    t = time.perf_counter()

    # part one
    nums = [ int(x) for x in re.findall(r'(-?\d+)', data)]
    print(f'part one {sum(nums)}')

    # part two
    data = json.loads(file)

    print(data)


