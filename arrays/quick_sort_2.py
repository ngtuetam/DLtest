def qsort(nums) -> None:
    def qsort_helper(nums, l: int, r: int) -> None:
        if l >= r: 
            return

        p = partition(nums, l, r)
        qsort_helper(nums, l, p - 1)
        qsort_helper(nums, p + 1, r)

    def partition(nums, l: int, r: int) -> int:
        pivot, p = nums[r], r

        i = l
        while i < p:
            if nums[i] > pivot: 
                nums[i], nums[p - 1] = nums[p - 1], nums[i]
                nums[p], nums[p - 1] = nums[p - 1], nums[p]
                i-=1
                p -= 1
            i += 1

        return p
        
    qsort_helper(nums, 0, len(nums) - 1)




my_list = [4,6,1,7,3,2,5]
nums = [2,0,2,1,1,0]
k = [0,8,4,2,2,1,3,0,6,2,5,7,9,9]
qsort(nums)
print(nums)

