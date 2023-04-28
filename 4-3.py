n = int(input("Enter the number of processes: "))
bt = list(map(int, input("Enter the burst times: ").split()))
rem = bt.copy()
h = int(input("Enter the time slice: "))
t=0
wt = [0]*n
while True:
    found = False
    for i in range(n):
        if rem[i] > 0:
            found = True
            if rem[i] > h:
                t += h
                rem[i] -= h
            else:
                t += h
                wt[i] = t - bt[i]
                rem[i] = 0
    if found == False:
        break
tt = [(wt[i]+bt[i]) for i in range(n)]
print(bt,wt,tt)
print(sum(wt)/n)
print(sum(tt)/n)

"ROUND"