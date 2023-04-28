def fifo(x,s):
    frame = [x[i] for i in range(s)]
    count = 0
    hit = 0
    fault = s
    for i in range(s, len(x)):
        if count == s:
            count = 0
        if x[i] in frame:
            hit = hit + 1
        else:
            fault = fault + 1
            frame[count] = x[i]
            count = count + 1
    print("FIFO Hits:", hit)
    print("FIFO Misses:", fault)

def optimal(x,s):
    frame = [x[i] for i in range(s)]
    hit = 0
    fault = s
    ind = s
    las = [0 for i in range(s)]
    for i in range(s, len(x)):
        if x[i] in frame:
            hit = hit + 1
        else:
            fault = fault+1
            for j in range(s):
                if frame[j] not in x[ind:]:
                    las[j] = len(x)+1
                else:
                    las[j] = len(x[ind:]) - x[ind:][::-1].index(frame[j]) - 1
            frame[las.index(max(las))] = x[i]
        ind = ind + 1
    print("Optimal Hits: ", hit)
    print("Optimal Misses: ", fault)

def lru(x,s):
    frame = [x[i] for i in range(s)]
    hit = 0
    fault = s
    use = [0 for i in range(s)]
    for i in range(s, len(x)):
        if x[i] in frame:
            hit = hit + 1
            use[frame.index(x[i])] += 2
        else:
            fault = fault + 1
            frame[use.index(min(use))] = x[i]
            use[frame.index(x[i])] += 1
    print("LRU Hits:", hit)
    print("LRU Misses:", fault)                 
    

x = list(map(int, input("Enter the reference string:").split()))
s = int(input("Enter the size: "))
fifo(x,s)
optimal(x,s)
lru(x,s)
