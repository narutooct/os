from threading import Thread, Semaphore
buffer=[]
while(True):
    ch = int(input("Menu : 1.Produce 2.Consume 3.Exit: "))
    match ch:
        case 1:
            n = int(input("Enter buffer size: "))
            empty = Semaphore(n)
            full = Semaphore(0)
            mutex = Semaphore(1)
            for i in range(n):
                empty.acquire()
                mutex.acquire()
                buffer.append(i)
                mutex.release()
                full.release()
        case 2:
            item = 0
            if len(buffer) == 0:
                print("Buffer is empty")
                continue
            for i in range(len(buffer)):
                full.acquire()
                mutex.acquire()
                buffer.pop(0)
                item += 1
                mutex.release()
                empty.release()
            print("Consumed: ", item)
        case 3:
            print("Exiting")
            break