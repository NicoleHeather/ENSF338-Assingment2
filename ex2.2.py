import sys
import json
import matplotlib.pyplot as plt
import time
import threading
sys.setrecursionlimit(20000)

threading.stack_size(33554432)

with open("ex2data.json", 'r') as data_file:
    data = json.load(data_file)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):   
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

timings = []

for arr in data:
    start = float(time.time())
    func1(arr, 0, 999)
    end = float(time.time())
    total = float(end - start)
    timings.append(total)

print(timings)
    
plt.plot(timings)
plt.ylabel("Time (s)")
plt.xlabel("Array Number")
plt.show()