def factorial(n):
    if n == 1:
        return 1

    else:
        return n * factorial(n-1)
    
print(factorial(5))


def fib_rec(n):
    if n == 0 or n == 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

print(fib_rec(7))