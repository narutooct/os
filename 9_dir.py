import os


def createdir():
    dir_list = list(map(input("Enter the directory names: ").split()))
    for i in dir_list:
        os.mkdir(i)

def createdir_2():
    dir_path = input("Enter the path: ")
    dir_list = list(map(input("Enter the directory names: ").split()))
    for i in dir_list:
        os.mkdir(os.path.join(dir_path,i))
    
def createfile():
    file_path = input("Enter the file path: ")
    file_name = input("enter the file name")
    if os.path.exists(os.path.join(file_path,file_name)):
        print("file exists")
    else:
        f = open(os.path.join(file_path,file_name),"w")

def display():
    pa = input("Enter the path:")
    print(os.listdir(pa))

def delte_file():
    file_path = input("Enter the file path: ")
    file_name = input("enter the file name")
    if os.path.exists(os.path.join(file_path,file_name)):
        os.remove(os.path.join(file_path,file_name))
    else:
        print("no file")

def rmdirs():
    dir_path = input("Enter the path: ")
    dir_name = input("Enter the dir name: ")
    try:
        os.rmdir(os.path.join(dir_path, dir_name))
        return
    except OSError as ose:
        files = os.listdir(os.path.join)
        for i in files:
            os.remove(i)
        rmdirs()


while(True):
    c = int(input("Enter your choice: \n1.Create root directories \n2.Create level2 directories \n3.Create File \n4.Display \n5.Remove Directory \n6.Remove File \n7.Exit \n"))
    if c == 1:
        createdir()
    elif c == 2:
        createdir_2()
    elif c == 3:
        createfile()
    elif c == 4:
        display()
    elif c == 5:
        rmdirs()
    elif c == 6:
        delte_file()
    elif c == 7:
        print("~~~~~~EXITING~~~~~~")
        break
    else:
        print("Invalid choice")