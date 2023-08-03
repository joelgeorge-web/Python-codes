#time taken to run a fibonacci sequence

import time

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)
    
start = time.time()
a = int(input("Enter a number: "))
print(fib(a))
end = time.time()
print(end - start)
