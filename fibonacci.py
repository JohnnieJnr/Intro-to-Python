def fib_rec(n):
    if n == 0 or n == 1:
        return n

    return fib_rec(n-1) + fib_rec(n-2)
    
print(list(range(1,21)))  
print(list(map(fib_rec, range(1,21))))