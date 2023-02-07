def fibo(n):
    memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n <= 2:
        return 1
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

