def solve1():
    with open('in.txt') as f:
        mat = []
        mat.append("." * 142)
        for row in f:
            row = "." + row.strip() + "."
            mat.append(row)
        mat.append("." * 142)
    sum = 0
    for i in range(1, len(mat) - 1):
        j = 1
        while j < len(mat[i]) - 1:
            if j + 3 < len(mat[i]) and mat[i][j].isdigit() and mat[i][j + 1].isdigit() and mat[i][j + 2].isdigit():
                # size 3
                if (mat[i - 1][j - 1] != "." or mat[i - 1][j] != "." or mat[i - 1][j + 1] != "." or mat[i - 1][
                    j + 2] != "." or mat[i - 1][j + 3] != "." or
                        mat[i][j - 1] != "." or mat[i][j + 3] != "." or
                        mat[i + 1][j - 1] != "." or mat[i + 1][j] != "." or mat[i + 1][j + 1] != "." or mat[i + 1][
                            j + 2] != "." or mat[i + 1][j + 3] != "."):
                    sum += int(mat[i][j:j + 3])
                j += 4
            elif j + 2 < len(mat[i]) and mat[i][j].isdigit() and mat[i][j + 1].isdigit():
                # size 2
                if (mat[i - 1][j - 1] != "." or mat[i - 1][j] != "." or mat[i - 1][j + 1] != "." or mat[i - 1][
                    j + 2] != "." or
                        mat[i][j - 1] != "." or mat[i][j + 2] != "." or
                        mat[i + 1][j - 1] != "." or mat[i + 1][j] != "." or mat[i + 1][j + 1] != "." or mat[i + 1][
                            j + 2] != "."):
                    sum += int(mat[i][j:j + 2])
                j += 3
            elif mat[i][j].isdigit():
                # size 1
                if (mat[i - 1][j - 1] != "." or mat[i - 1][j] != "." or mat[i - 1][j + 1] != "." or
                        mat[i][j - 1] != "." or mat[i][j + 1] != "." or
                        mat[i + 1][j - 1] != "." or mat[i + 1][j] != "." or mat[i + 1][j + 1] != "."):
                    sum += int(mat[i][j])
                j += 2
            else:
                j += 1
    print(sum)


def solve2():
    with open('in.txt') as f:
        mat = []
        mat.append("." * 146)
        for row in f:
            row = "..." + row.strip() + "..."
            mat.append(row)
        mat.append("." * 146)
    sum = 0
    for i in range(1, len(mat) - 1):
        j = 3
        while j < len(mat[i]) - 3:
            if mat[i][j] == "*":
                dx = 1
                sx = 1
                downdx = 1
                downsx = 1
                down = 1
                upsx = 1
                updx = 1
                up = 1
                cnt = 0
                if (mat[i][j + 1].isdigit()):
                    cnt += 1
                    # est
                    if mat[i][j + 1].isdigit() and mat[i][j + 2].isdigit() and mat[i][j + 3].isdigit():
                        # size 3
                        dx = int(mat[i][j + 1:j + 4])
                    elif mat[i][j + 1].isdigit() and mat[i][j + 2].isdigit():
                        # size 2
                        dx = int(mat[i][j + 1:j + 3])
                    elif mat[i][j + 1].isdigit():
                        # size 1
                        dx = int(mat[i][j + 1:j + 2])
                if (mat[i][j - 1].isdigit()):
                    cnt += 1
                    # ovest
                    if (mat[i][j - 1].isdigit() and mat[i][j - 2].isdigit() and mat[i][j - 3].isdigit()):
                        # size 3
                        sx = int(mat[i][j - 3:j])
                    elif (mat[i][j - 1].isdigit() and mat[i][j - 2].isdigit()):
                        # size 2
                        sx = int(mat[i][j - 2:j])
                    elif mat[i][j - 1].isdigit():
                        # size 1
                        sx = int(mat[i][j - 1:j])
                # sud
                # are there two numbers?
                if (not mat[i + 1][j].isdigit()):
                    # sud-est
                    if mat[i + 1][j + 1].isdigit() and mat[i + 1][j + 2].isdigit() and mat[i + 1][j + 3].isdigit():
                        # size 3
                        downdx = int(mat[i + 1][j + 1:j + 4])
                        cnt += 1
                    elif mat[i + 1][j + 1].isdigit() and mat[i + 1][j + 2].isdigit():
                        # size 2
                        downdx = int(mat[i + 1][j + 1:j + 3])
                        cnt += 1
                    elif mat[i + 1][j + 1].isdigit():
                        # size 1
                        downdx = int(mat[i + 1][j + 1:j + 2])
                        cnt += 1
                    # sud-ovest
                    if (mat[i + 1][j - 1].isdigit() and mat[i + 1][j - 2].isdigit() and mat[i + 1][j - 3].isdigit()):
                        # size 3
                        downsx = int(mat[i + 1][j - 3:j])
                        cnt += 1
                    elif (mat[i + 1][j - 1].isdigit() and mat[i + 1][j - 2].isdigit()):
                        # size 2
                        downsx = int(mat[i + 1][j - 2:j])
                        cnt += 1
                    elif mat[i + 1][j - 1].isdigit():
                        # size 1
                        downsx = int(mat[i + 1][j - 1:j])
                        cnt += 1
                else:
                    # sud
                    if mat[i + 1][j + 1].isdigit() and mat[i + 1][j + 2].isdigit():
                        # size 3
                        down = int(mat[i + 1][j:j + 3])
                    elif mat[i + 1][j - 1].isdigit() and mat[i + 1][j - 2].isdigit():
                        # size 3
                        down = int(mat[i + 1][j - 2:j + 1])
                        pass
                    elif mat[i + 1][j + 1].isdigit() and mat[i + 1][j - 1].isdigit():
                        # size 3
                        down = int(mat[i + 1][j - 1:j + 2])
                    elif mat[i + 1][j - 1].isdigit():
                        # size 2
                        down = int(mat[i + 1][j - 1:j + 1])
                    elif mat[i + 1][j + 1].isdigit():
                        # size 2
                        down = int(mat[i + 1][j:j + 2])
                    else:
                        # size 1
                        down = int(mat[i + 1][j])
                    cnt += 1
                # nord
                # are there two numbers?
                if (not mat[i - 1][j].isdigit()):
                    # nord-est
                    if mat[i - 1][j + 1].isdigit() and mat[i - 1][j + 2].isdigit() and mat[i - 1][j + 3].isdigit():
                        # size 3
                        updx = int(mat[i - 1][j + 1:j + 4])
                        cnt += 1
                    elif mat[i - 1][j + 1].isdigit() and mat[i - 1][j + 2].isdigit():
                        # size 2
                        updx = int(mat[i - 1][j + 1:j + 3])
                        cnt += 1
                    elif mat[i - 1][j + 1].isdigit():
                        # size 1
                        updx = int(mat[i - 1][j + 1])
                        cnt += 1
                    # nord-ovest
                    if (mat[i - 1][j - 1].isdigit() and mat[i - 1][j - 2].isdigit() and mat[i - 1][j - 3].isdigit()):
                        # size 3
                        upsx = int(mat[i - 1][j - 3:j])
                        cnt += 1
                    elif (mat[i - 1][j - 1].isdigit() and mat[i - 1][j - 2].isdigit()):
                        # size 2
                        upsx = int(mat[i - 1][j - 2:j])
                        cnt += 1
                    elif mat[i - 1][j - 1].isdigit():
                        # size 1
                        upsx = int(mat[i - 1][j - 1:j])
                        cnt += 1
                else:
                    # nord
                    if mat[i - 1][j + 1].isdigit() and mat[i - 1][j + 2].isdigit():
                        # size 3
                        up = int(mat[i - 1][j:j + 3])
                    elif mat[i - 1][j - 1].isdigit() and mat[i - 1][j - 2].isdigit():
                        # size 3
                        up = int(mat[i - 1][j - 2:j + 1])
                        pass
                    elif mat[i - 1][j + 1].isdigit() and mat[i - 1][j - 1].isdigit():
                        # size 3
                        up = int(mat[i - 1][j - 1:j + 2])
                    elif mat[i - 1][j - 1].isdigit():
                        # size 2
                        up = int(mat[i - 1][j - 1:j + 1])
                    elif mat[i - 1][j + 1].isdigit():
                        # size 2
                        up = int(mat[i - 1][j:j + 2])
                    else:
                        # size 1
                        up = int(mat[i - 1][j])
                    cnt += 1
                if (cnt >= 2):
                    sum = sum + (dx * sx * downdx * downsx * down * upsx * updx * up)
            j += 1
    print(sum)


if __name__ == '__main__':
    solve1()
    solve2()
