'''
problem: sort color _ leet code
using quick sort
'''
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def qsort_helper(nums, l: int, r: int) -> None:
            if l >= r: return

            p = partition(nums, l, r)
            qsort_helper(nums, l, p - 1)
            qsort_helper(nums, p + 1, r)
        def quick_sort(my_list):
            qsort_helper(my_list, 0, len(my_list)-1)

        def partition(nums, l: int, r: int) -> int:
            pivot, p = nums[r], r
            i = l
            while i < p:
                if nums[i] > pivot: 
                    nums[i], nums[p - 1] = nums[p - 1], nums[i]
                    nums[p], nums[p - 1] = nums[p - 1], nums[p]
                    i -= 1
                    p -= 1
                i += 1
            return p
            
        quick_sort(nums)
        