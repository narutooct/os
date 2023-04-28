n = int(input("Enter the number of processes: "))
bt = list(map(int, input("Enter the burst times: ").split()))
wt = [0]
for i in range(n-1):
    wt.append(wt[i]+bt[i])
tt = [(wt[i]+bt[i]) for i in range(n)]
print(bt,wt,tt)
print(sum(wt)/n)
print(sum(tt)/n)

"FCFS"