import time
from threading import *
s=Semaphore(2)
def wish(name):
    s.acquire()
    for i in range(10):
        print("good evening",end=" ")
        time.sleep(2)
        print(name)
    s.release()


t1=Thread(target=wish,args=('jose',))

t2=Thread(target=wish,args=('mitch',))
t3=Thread(target=wish,args=('mart',))
t4=Thread(target=wish,args=('solomon',))
t5=Thread(target=wish,args=('janu',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()