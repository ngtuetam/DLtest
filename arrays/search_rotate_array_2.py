# find in left sorted part or right part

def search(nums, target: int) -> int:
    n = len(nums)
    l = 0
    r = n -1
    while l <= r:
        m = l + (r-l)//2
        if nums[m] == target:
            return m
        if nums[m] >= nums[l]:
            if nums[l] <= target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if nums[m] <= target <= nums[r]:
                l = m+1
            else:
                r = m - 1
    return -1


nums = [8,7,6,5,4,3,2,1]
print(search(nums,7))