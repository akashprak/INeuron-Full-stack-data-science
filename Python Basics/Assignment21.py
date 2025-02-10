import multiprocessing
import time
from random import randint
from datetime import datetime

def process1():
    time.sleep(randint(1,5))
    print(f'process 1 time: {datetime.now().time()}')

def process2():
    time.sleep(randint(1,5))
    print(f'process 2 time: {datetime.now().time()}')

def process3():
    time.sleep(randint(1,5))
    print(f'process 3 time: {datetime.now().time()}')

if __name__=='__main__':

    p1 = multiprocessing.Process(target=process1)
    p2 = multiprocessing.Process(target=process2)
    p3 = multiprocessing.Process(target=process3)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()