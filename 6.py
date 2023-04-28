def bak(np,nr,allo,max,avail):
    need = [[0 for i in range(nr)]for i in range(np)]
    for i in range(np):
        for j in range(nr):
            need[i][j] = max[i][j] - allo[i][j]
    work = avail
    count = 0
    safe = [0] * np
    finish = [0] * np
    while(count < np):
        found = False
        for i in range(np):
            if finish[i] == 0:
                for j in range(nr):
                    if need[i][j] > work[j]:
                        break
                    if j == nr-1:
                        for k in range(nr):
                            work[k] += allo[i][k]
                        safe[count] = i
                        finish[i] = 1
                        found = True
                        count += 1
        if found == False:
            print('no safe')
            return
    print(safe)
    print('safe')
    return

np = int(input("Enter number of processes: "))
nr = int(input("Enter number of resources"))
allo = []
max = []
for i in range(np):
    allo.append(list(map(int, input("enter allo: ").split())))
    max.append(list(map(int, input("enter max: ").split())))
avail = list(map(int, input("enter avail: ").split()))
bak(np,nr,allo,max,avail)