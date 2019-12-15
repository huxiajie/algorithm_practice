# 递归法 O(2^n)
def fib_recursion(n):
    if n < 0:
        return "error"
    elif n == 0 or n == 1:
        return 1
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)

# 递推法 O(n)
def fib_derivation(n):
    if n < 0:
        return "error"
    f0 = f1 = 1
    # n=0 or n=1,都不会紧循环
    for i in range(1, n):
        f0, f1 = f1, f0 + f1
    return f1
