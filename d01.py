mappa = {"one": 1,
         "two": 2,
         "three": 3,
         "four": 4,
         "five": 5,
         "six": 6,
         "seven": 7,
         "eight": 8,
         "nine": 9}

def solve1():
    with open('in.txt') as f:
        sum = 0
        for line in f:
            line = line.strip()
            minl = len(line)
            maxl = -1
            for value in mappa.values():
                lv = line.find(str(value))
                rv = line.rfind(str(value))
                if lv != -1 and lv < minl:
                    minl = lv
                    minv = value
                if rv != -1 and rv > maxl:
                    maxl = rv
                    maxv = value
            sum = sum + minv * 10 + maxv
    print(sum)

def solve2():
    with open('in.txt') as f:
        sum = 0
        for line in f:
            line = line.strip()
            minl = len(line)
            maxl = -1
            for key, value in mappa.items():
                lk = line.find(key)
                lv = line.find(str(value))
                rk = line.rfind(key)
                rv = line.rfind(str(value))
                if lk != -1 and lk < minl:
                    minl = lk
                    minv = mappa[key]
                if lv != -1 and lv < minl:
                    minl = lv
                    minv = value
                if rk != -1 and rk > maxl:
                    maxl = rk
                    maxv = mappa[key]
                if rv != -1 and rv > maxl:
                    maxl = rv
                    maxv = value
            sum = sum + minv * 10 + maxv
    print(sum)


if __name__ == '__main__':
    solve1()
    solve2()

