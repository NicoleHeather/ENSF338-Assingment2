import timeit 

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
    
    original = []
    optimized = []
    for i in range(36):
        original.append(func(i))
        optimized.append(func2(i))