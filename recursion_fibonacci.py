def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
fib_num=fibo(5)
print('5th fibonacci is ',fib_num)