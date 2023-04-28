import threading
read_count = 0
read_mutex = threading.Semaphore(1)
write_mutex = threading.Semaphore(1)
def reader(i):
    read_mutex.acquire()
    global read_count
    read_count += 1
    if read_count == 1:
        write_mutex.acquire()
    read_mutex.release()
    print(f"Reader {i} is reading from the shared resource...")
    read_mutex.acquire()
    read_count -= 1
    if read_count == 0:
        write_mutex.release()
    read_mutex.release()
def writer(i):
    write_mutex.acquire()
    print(f"Writer {i} is writing to the shared resource...")
    write_mutex.release()
reader_threads = [threading.Thread(target=reader, args=(i,)) for i in range(5)]
writer_threads = [threading.Thread(target=writer, args=(i,)) for i in range(2)]
for thread in reader_threads:
    thread.start()
for thread in writer_threads:
    thread.start()