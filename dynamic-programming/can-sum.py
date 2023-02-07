def canSum(targetsum, nums):
    if targetsum == 0:
        return True
    if targetsum < 0:
        return False
    for num in nums:
        remain = targetsum - num
        if canSum(remain, nums) == True:
            return True
    return False

print(canSum(8, [3,3,9]))