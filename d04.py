def solve2():
    cards = {}
    for i in range(1,204):
        cards[i]=1
    with open('in.txt') as f:
        numbercard = 1
        for row in f:
            row = row.strip().split("|")
            winning_num = set(row[0].split(":")[1].split(" "))
            winning_num.remove("")
            my_num = set(row[1].split(" "))
            my_num.remove("")
            mathing_number = winning_num.intersection(my_num)
            for update in range(numbercard+1,numbercard+1+len(mathing_number)):
                cards[update]+=cards[numbercard]
            numbercard+=1
    s = sum(cards.values())
    print(s)

def solve1():
    with open('in.txt') as f:
        sum = 0
        for row in f:
            row = row.strip().split("|")
            winning_num = set(row[0].split(":")[1].split(" "))
            winning_num.remove("")
            my_num = set(row[1].split(" "))
            my_num.remove("")
            exp = len(winning_num.intersection(my_num))-1
            if exp>=0:
                sum += 2**exp
    print(sum)

if __name__ == '__main__':
    solve1()
    solve2()