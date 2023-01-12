# fill all
def findDisappearedNumbers(nums):
    check = [i for i in range(1,len(nums)+1)]
    nums = list(set(nums))
    for i in range(len(nums)):
        if nums[i] in check:
            check.remove(nums[i])
        return check

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))
  

