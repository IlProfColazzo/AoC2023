import math


def solve1():
    with open('in.txt') as f:
        time = [int(_) for _ in f.readline().split(":")[1].strip().split(" ") if _ != ""]
        distance = [int(_) for _ in f.readline().split(":")[1].strip().split(" ") if _ != ""]
    p = 1
    for t, d in zip(time, distance):
        delta = math.sqrt((t * t) - (4 * d))
        min = int((-t + delta) / (-2)) + 1
        max = math.ceil((-t - delta) / (-2)) - 1
        n = max - min + 1
        p *= n
    print(p)


def solve2():
    with open('in.txt') as f:
        t = int(f.readline().split(":")[1].strip().replace(" ", ""))
        d = int(f.readline().split(":")[1].strip().replace(" ", ""))
        delta = math.sqrt((t * t) - (4 * d))
        min = int((-t + delta) / (-2)) + 1
        max = math.ceil((-t - delta) / (-2)) - 1
        n = max - min + 1
    print(n)


if __name__ == '__main__':
    solve1()
    solve2()
