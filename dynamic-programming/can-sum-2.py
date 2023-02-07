def canSum(targetsum, nums):
    memo = {}
    if targetsum in memo:
        return memo[targetsum]
    if targetsum == 0:
        return 1
    if targetsum < 0:
        return False
    for num in nums:
        remain = targetsum - num
        if canSum(remain, nums) == True:
            memo[targetsum] = True
            return True
    memo[targetsum] = False
    return False

print(canSum(7, [1,1,1,1,1]))