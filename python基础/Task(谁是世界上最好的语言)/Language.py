Language_Teams = ['Java', 'C++', 'C', 'Python','JavaScript', 'C#', 'Swift', 'Golang', 'PHP', 'Ruby']


def CalcAscii(st):
    sum_ascii = 0
    for chac in st:
        sum_ascii += ord(chac)
    return sum_ascii


def CompeteWin(a, b):
    if CalcAscii(a) > CalcAscii(b):
        return a
    else:
        return b


def CompeteLose(a, b):
    if CalcAscii(a) < CalcAscii(b):
        return a
    else:
        return b


def Check(All_Competitor):
    tot = 0
    Now_Language = ['0'] * 4
    for member in All_Competitor:
        tot += 1
        # print(member)
        if tot > 4:
            return 0
        if member not in Language_Teams:
            return 0
        if member in Now_Language:
            return 0
        Now_Language[tot - 1] = member
    if tot < 4:
        return 0
    else:
        return 1


competitor = input("Which teams are playing in the finals this year?").split(',')
if Check(competitor):
    print(*competitor, sep=',')
    winner = ['0'] * 4
    loser = ['0'] * 4
    winner[0] = CompeteWin(competitor[0], competitor[1])
    loser[0] = CompeteLose(competitor[0], competitor[1])
    print(winner[0], "defeated", loser[0], "in the First Semi-Final.")
    winner[1] = CompeteWin(competitor[2], competitor[3])
    loser[1] = CompeteLose(competitor[2], competitor[3])
    print(winner[1], "defeated", loser[1], "in the Second Semi-Final.")
    winner[2] = CompeteWin(winner[0], loser[1])
    loser[2] = CompeteLose(winner[0], loser[1])
    print(winner[2], "defeated", loser[2], "in the Preliminary Final.")
    winner[3] = CompeteWin(winner[1], winner[2])
    loser[3] = CompeteLose(winner[1], winner[2])
    print(winner[3], "defeated", loser[3], "in the Grand Final.")
    print(winner[3], "win the Premiership!")
else:
    print("Please check your list of languages.")





