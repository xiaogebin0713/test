import  threading
from time import sleep
from threading import Lock

l = Lock()
sum = 0
def test(name, ID):
    global sum
    print(name, ID)
    sleep(5)
    l.acquire()
    sum = sum + 1
    l.release()
    print(sum, ID)
    print("test")

if __name__ == "__main__":
    # print("test")
    threadLists = []
    # global sum
    for i in range(1, 5, 1):
        t = threading.Thread(target=test, args=("testname", i), daemon=True)
        threadLists.append(t)
        t.start()
        
    
    for i in threadLists:
        t.join()
    # print("sum:", sum)
    # print("end")