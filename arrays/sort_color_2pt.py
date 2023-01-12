def sortColors(nums):
    n = len(nums)
    p0 = 0
    p = 0
    p2 = n - 1
    while (p<=p2):
        if nums[p] == 0:
            nums[p] = nums[p0]
            nums[p0] = 0
            p0+=1
            p+=1
        elif nums[p] == 2:
            nums[p] = nums[p2]
            nums[p2] = 2
            p2 -= 1
        else:
            p +=1