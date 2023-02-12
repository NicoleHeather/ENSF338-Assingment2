import sys
import threading
import json
import matplotlib.pyplot as plt
import time
sys.setrecursionlimit(20000)
threading.stack_size(33554432)

with open("ex2data.json", 'r') as data_file:
    data = json.load(data_file)

def func1(arr, low, high):
    if low < high:
        pivot = func3(arr, low, high)
        pi = func2(arr, low, high, pivot)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func3(array, start, end):
    add = start + end
    middle = add // 2
    pivot = end
    if array[start] < array[middle]:
        if array[middle] < array[end]:
            pivot = middle
    elif array[start] < array[end]:
        pivot = start
    return pivot

def func2(array, start, end, pivot):
    pivot_value = array[pivot]
    array[pivot], array[start] = array[start], array[pivot]
    border = start
    for i in range(start, end):
        if array[i] < pivot_value:
            border += 1
            array[i], array[border] = array[border], array[i]
    array[start], array[border] = array[border], array[start]
    return border

timings = []

for arr in data:
    start = float(time.time())
    func1(arr, 0, len(arr)-1)
    end = float(time.time())
    total = float(end - start)
    timings.append(total)

print(timings)
    
plt.plot(timings)
plt.ylabel("Time (s)")
plt.xlabel("Array Number")
plt.show()