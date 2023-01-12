def binary_search(nums, target):
    n = len(nums)
    l = 0
    r = n-1
    while l <= r:
        m = l + ((r-l)//2)
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

nums = [7,8,9,0,1,2]
print(binary_search(nums,1))





'''
n = 6
l = 0, n = 5, m = 2
=> 4
2 3 4 5 8 50
t = 8
'''

