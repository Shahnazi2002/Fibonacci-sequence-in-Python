def isFibonacci(n):
    s = []
    a, b = 0, 1
    while a <= n:
        s = [a]
        a, b = b, a + b
    if n in s:
        return True
    else:
        return False


print(isFibonacci(8))
