def solve1():
    with open('in.txt') as f:
        colours = {"red": 12,
                 "green": 13,
                 "blue": 14}
        sum = 0
        for game, line in enumerate(f):
            subsets = line.strip().split(":")[1].split(";")
            impossible = False
            for subset in subsets:
                cubes = subset.split(",")
                for cube in cubes:
                    colour = cube.strip().split(" ")[1]
                    value = int(cube.strip().split(" ")[0])
                    if value > colours[colour]:
                        impossible = True
                        # print(line)
                        break
                if impossible:
                    break
            if not impossible:
                sum += (game + 1)
        print(sum)


def solve2():
    with open('in.txt') as f:
        sum = 0
        for line in f:
            colours = {"red": 0,
                     "green": 0,
                     "blue": 0}
            subsets = line.strip().split(":")[1].split(";")
            for subset in subsets:
                cubes = subset.split(",")
                for cube in cubes:
                    colour = cube.strip().split(" ")[1]
                    value = int(cube.strip().split(" ")[0])
                    if value > colours[colour]:
                        colours[colour] = value
            p = colours["red"] * colours["green"] * colours["blue"]
            sum += p
        print(sum)


if __name__ == '__main__':
    solve1()
    solve2()