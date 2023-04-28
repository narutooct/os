def fcfs(n,h,t):
    sum = 0
    for i in range(n):
        sum += abs(h-t[i])
        print(abs(h - t[i]))
        h = t[i]
    print(sum)

def sstf(n,h,t):
    sum = 0
    for i in range(n):
        min = float('inf')
        for j in range(n):
            if min > abs(t[j] - h) and t[j] != -1:
                min = abs(t[j] - h)
                k = j
        print(min)
        sum += min
        h = t[k]
        t[k] = -1
    print(sum)

n = int(input("enter the number of tracks"))
h = int(input("Enter the head position: "))
t = list(map(int, input("Enter the tracks: ").split()))
fcfs(n,h,t)
print("sstf")
sstf(n,h,t)