def binary_search_rec(nums, target, l, r):
    m = l + ((r-l)//2)
    if l > r:
        return  -1
    if nums[m] == target:
        return m
    elif nums[m] < target:
        return binary_search_rec(nums, target, m+1, r)
    else:
        return binary_search_rec(nums, target, l, m-1)

def binary_search(nums, target):
  	return binary_search_rec(nums, target, 0, len(nums) - 1)

nums = [2, 3 ,4, 5, 8 ,50]
print(binary_search(nums,8))



