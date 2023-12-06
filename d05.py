def solve1():
    with open('in.txt') as f:
        seeds = [int(_) for _ in f.readline().split(":")[1].strip().split(" ")]
        f.readline()
        a = [list() for _ in range(7)]
        for i in range(7):
            f.readline()
            row = f.readline()
            while row != "\n":
                a[i].append(row)
                row = f.readline()
        number = []
        for seed in seeds:
            for i in range(7):
                for rule in a[i]:
                    l = [int(_) for _ in rule.strip().split(" ")]
                    if seed >= l[1] and seed < l[1] + l[2]:
                        seed = seed - l[1] + l[0]
                        break
            number.append(seed)
        print(min(number))


if __name__ == '__main__':
    solve1()
