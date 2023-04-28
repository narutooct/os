# def cma(np, nb, b, p): 
#     allo = [-1] * np 
#     b1 = b.copy()     
#     print()     
#     print("First Fit Algorithm: ")     
#     for i in range(np):         
#         for j in range(nb):             
#             if b[j] >= p[i]: 
#                 allo[i] = j                 
#                 b[j] = 0 
#                 break 
#     print("Process No.\tProcess Size\tBlock no.")     
#     for i in range(np): 
#         print(i + 1, "\t\t", p[i], "\t\t", end = " ")         
#         if allo[i] != -1: 
#             print(allo[i] + 1)         
#         else: 
#             print("Not Allocated") 
#     print() 
# #.........................................................
#     print("Best Fit Algorithm: ")     
#     b = b1.copy()     
#     allo = [-1] * np     
#     for i in range(np):         
#         best = -1         
#         for j in range(nb):             
#             if b[j] >= p[i]:                 
#                 if best == -1:                     
#                     best = j                 
#                 elif b[j] < b[best]:                     
#                     best = j         
#         if best != -1: 
#             allo[i] = best             
#             b[best] = 0     
#     print("Process No.\tProcess Size\tBlock no.")     
#     for i in range(np): 
#         print(i + 1, "\t\t", p[i], "\t\t", end = " ")         
#         if allo[i] != -1:             
#             print(allo[i] + 1)         
#         else: 
#             print("Not Allocated") 
    
#     print() 
# #..............................................................
#     print("Worst Fit Algorithm: ")     
#     b = b1.copy()     
#     allo = [-1] * np     
#     for i in range(np): 
#         worst = -1         
#         for j in range(nb): 
#             if b[j] >= p[i]: 
#                 if worst == -1:                     
#                     worst = j                 
#                 elif b[j] > b[worst]: 
#                     worst = j         
#         if worst != -1: 
#             allo[i] = worst             
#             b[worst] = 0     
#     print("Process No.\tProcess Size\tBlock no.")     
#     for i in range(np): 
#         print(i + 1, "\t\t", p[i], "\t\t", end = " ")
#         if allo[i] != -1:
#             print(allo[i] + 1)
#         else:
#             print("Not Allocated") 
# np = int(input("Enter number of processes: "))
# p = list(map(int, input("Enter size of each process: ").split()))
# nb = int(input("Enter number of blocks: "))
# b = list(map(int, input("Enter size of each block: ").split()))
# cma(np, nb, b, p) 

def cma(np,p,nb,b):
    b1 = b.copy()
    allo = [-1]*np
    print("FIFO")
    for i in range(np):
        best = -1
        for j in range(nb):
            if best == -1:
                best = j
            elif b[j] < b[best]:
                best = j
        if best[i] != -1:
            allo[i] = best
            b[best] = 0


np = int(input("Enter the number of processes: "))
p = list(map(int, input("Enter the processes").split()))
nb = int(input("Enter the number of resources: "))
b = list(map(int, input("Enter the blocks: ").split()))

cma(np,p,nb,b)
