import time
import json

path = []
sum = 0


# this isnt working right now
# def walk(d):
#     global path, sum
#     for k, v in d.items():
#         if isinstance(v, int):
#             path.append(k)
#             sum = sum + int(v)
#             path.pop()
#         elif v is None:
#             path.append(k)
#             ## do something special
#             path.pop()
#         elif isinstance(v, dict):
#             path.append(k)
#             walk(v)
#             path.pop()
#         # else:
#         #     null
#     return sum


if __name__ == '__main__':
    # get input
    file = open('../../input/day12/input.json').read()
    # data = json.loads(file)
    data = json.loads(json.dumps('[1,2,3]'))
    # data =  json.dumps({"a":2,"b":4})
    t = time.perf_counter()
    # part one
    # up = data.count('(')
    # down = data.count(')')
    # print(f"The sum is {walk(data)}")
    # print(data)
    print(len(data.values()))
    # part two
    # floor = 0
    # position = 0
    # for c in data:
    #     position += 1
    #     floor = floor + 1 if c == '(' else floor - 1
    #     if floor == -1:
    #         print(f'Entered that basement at position {position}')
    #         print(f'Time taken {time.perf_counter() - t} seconds')
    #         exit(0)
    #
