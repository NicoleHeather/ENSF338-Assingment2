import timeit 
import matplotlib 
from matplotlib import pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

def func2(n, storage={}):
    if n == 0 or n == 1:
        return n
    else:
        if n in storage:
            return storage[n]
        else:
            storage[n] = func2(n-1) + func2(n-2)
            return storage[n]
        
if __name__ == "__main__":
        
    original_time = []
    optomized_time = []
    for i in range(36):    
        time_og = timeit.timeit(lambda:func(i), number = 1)
        time_op = timeit.timeit(lambda:func2(i), number = 1)
        original_time.append(time_og)
        optomized_time.append(time_op)
        
    linechart1 = plt.plot(range(1, 37), original_time, 'g')
    linechart2 = plt.plot(range(1, 37), optomized_time, 'b')
    plt.legend(['Unoptomized', 'Optomized'], loc = 1)
    plt.ylabel('Time taken(s)')
    plt.xlabel('Number(0-35)')
    plt.show()