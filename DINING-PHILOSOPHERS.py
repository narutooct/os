from random import choice
global a
def wait(process_num):
    global a
    a[process_num] -= 1
def signal(process_num):
    global a
    a[process_num] += 1
a = [1,1,1,1,1]
while(1):
    i=0
    process_nums = [0, 1, 2, 3, 4]
    copy1 = process_nums[:]
    copy2 = process_nums[:]
    p = int(input("1.One can eat at a time\n2.Two can eat at a time\n3.exit\n"))
    if (p == 1):
        while(i<5):
            rand_proc = choice(process_nums)
            wait(rand_proc)
            wait((rand_proc+1)%5)
            print("P"+str(rand_proc)+" is granted to eat")
            print("P"+str((rand_proc+1)%len(copy1))+" is waiting")
            print("P"+str((rand_proc+len(copy1)-1)%len(copy1))+" is waiting\n")
            signal(rand_proc)
            signal((rand_proc + 1) % 5)
            process_nums.remove(rand_proc)
            i += 1
            if (len(process_nums) == 0):
                break
    elif (p == 2):
        j = 0
        while (j < 5):
            rand_proc = choice(copy1)
            wait(rand_proc)
            wait((rand_proc + 1) % 5)
            print("P" + str(rand_proc) + " and" + " P" + str((rand_proc + 2) % 5) + " are granted to eat")
            print("P" + str((rand_proc + 3) % len(copy2)) + " is waiting")
            print("P" + str((rand_proc + 4) % len(copy2)) + " is waiting\n")
            signal(rand_proc)
            signal((rand_proc + 1) % 5)
            copy1.remove(rand_proc)
            i += 1
            if (len(copy1) == 0):
                break
    elif (p == 3):
        print("Thank You")
        break