def gridtravel(m,n):
    memo = {}
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = gridtravel(m-1,n) + gridtravel(m, n-1)
    return memo[key]


print(gridtravel(3,3))