# fill all
def findDisappearedNumbers(nums):
    res = []
    n = len(nums)
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] > 1:
            for j in range(nums[i]+1,nums[i+1]):
                res.append(j)
    if nums[n-1] < n:
        for i in range(nums[n-1]+1, n+1):
            res.append(i)
    if nums[0] > 1:
        for i in range(1, nums[0]):
            res.append(i)
    return res
    