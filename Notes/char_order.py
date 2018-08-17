import random

class Character:
    def __init__(self, id, name, stat, comp, min_time, max_time, pred, next, death, special):
        self.id = id                # Character Rank
        self.name = name            # Character Name
        self.stat = stat            # 1/0/-1 - Alive/Dead/Inactive
        self.comp = comp            # 1/0 - Complete/Incomplete
        self.min_time = min_time    # 1-10 (June-March)
        self.max_time = max_time    # 1-10 (June-March)
        self.pred = pred            # Follows a character's arc ([] if none)
        self.next = next            # Precedes a character's arc ([] if none)
        self.death = death          # Death Trigger ([] if none)
        self.special = special      # Special Properties

IY = Character(1, "Ichirou Yokohama", 1, 0, 2, 10, [], [2,3], [3,7], 0)
AI = Character(2, "Akira Ichibana", 1, 0, 1, 9, [1,3], [], [3,6,8,10], 0)
ST = Character(3, "Sumiko Tokubei", 1, 0, 1, 10, [1,5], [2], [5,8], 0)
IS = Character(4, "Inoue Shinozaki", 1, 0, 1, 9, [9], [8], [9], 0)
SR = Character(5, "Sayo Ronoroa", 1, 0, 1, 10, [], [3], [4,10], 1)
YS = Character(6, "Yoshiro Suzuki", 1, 0, 1, 9, [1,4], [8], [1,2], 1)
HK = Character(7, "Hiroshi Kano", 1, 0, 2, 10, [], [], [9], 0)
MH = Character(8, "Miyu Hirano", 1, 0, 6, 9, [1,4,5,6], [], [5], [1,4,6,10])
KK = Character(9, "Kyou Kirisaki", 1, 0, 1, 8, [], [4], [1,4], 0)
HY = Character(10, "Hikaru Yamamoto", 1, 0, 6, 10, [4,5], [], [4,8], 5)

chars = [IY, AI, ST, IS, SR, YS, HK, MH, KK, HY]
chars2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
poss = []
PQ = [10, 1, 2, 3, 4, 5, 9, 6, 7, 8]
l = 10

for i in range(1, 11):
    temp = []
    for j in range(l):
        if chars[j].min_time <= i <= chars[j].max_time and chars[j].comp == 0:
            temp.append(chars[j])
    poss.append(temp)


# Begin Randomization
for i in range(10):
    r = poss[i][random.randint(1,len(poss[PQ[i]-1]))]
    for j in range(10):
        if chars[r-1] in poss[j]:
            poss[j].pop(poss[j].index(chars[r-1]))
    chars.append(chars.pop(r-1))
    chars[-1].comp = 1
    chars2[PQ[i]-1] = chars[-1]
    l -= 1

for i in range(10):
    print i+1, chars2[i].name

