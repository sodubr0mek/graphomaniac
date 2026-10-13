edge = 7
matryca = [[0, 0, 1, 1, 0, 0, 0],
           [0, 0, 1, 0, 1, 1, 0],
           [1, 1, 0, 1, 0, 0, 0],
           [1, 0, 1, 0, 1, 0, 0],
           [0, 1, 0, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 1, 0]]


start = 0
finish = 6
slist = []
flist = []

def connect(point, sf):

    if sf == 0:
        table = []
        for i in range(edge):
            if matryca[point][i] == 1:
                table.append(i)
        slist.append(table)

    if sf == 1:
        table = []
        for i in range(edge):
            if matryca[point][i] == 1:
                table.append(i)
        flist.append(table)

connect(start, 0)
connect(finish, 1)

tie = 0
run = 1
level = 0
while(run != 0):

    for i in range(len(slist[level])):
        connect(slist[level][i], 0)

    if len(slist) > (level + 1):
        for i in range(len(slist)-level-2):
            for j in range(len(slist[-2])):
                if slist[-2][j] not in slist[-1]:
                    slist[-1].append(slist[-2][j])
            slist.pop(-2)

    for i in range(len(slist)-1):
        for j in range(len(slist[i])):
            if slist[i][j-1] in slist[-1]:
                slist[-1].remove(slist[i][j-1])

    if start in slist[-1]:
        slist[-1].remove(start)



    
    for i in range(len(flist[level])):
        connect(flist[level][i], 1)

    if len(flist) > (level + 1):
        for i in range(len(flist)-level-2):
            for j in range(len(flist[-2])):
                if flist[-2][j] not in flist[-1]:
                    flist[-1].append(flist[-2][j])
            flist.pop(-2)

    for i in range(len(flist)-1):
        for j in range(len(flist[i])):
            if flist[i][j-1] in flist[-1]:
                flist[-1].remove(flist[i][j-1])

    if finish in flist[-1]:
        flist[-1].remove(finish)





    for i in range(len(slist)):
        for j in range (len(slist[i])):
            for k in range(len(flist)):
                if slist[i][j] in flist[k]:
                    tie = slist[i][j]
                    run = 0
    level += 1




print(slist)
print(flist)
print(tie)

run2 = 1
#Dodać prowadzdenie drogi przez szukanie ścieżek do coraz wcześniejszych odnóg a







