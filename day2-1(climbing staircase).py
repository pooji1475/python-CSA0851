def fib(n):
    if(n<=1):
        return n
    else:
        return fib(n-1)+fib(n-2)
def ways(w):
    return fib(w+1)
a=int(input("Enter no of stairs: "))
print("Number of ways = ",ways(a))
