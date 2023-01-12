# choose random element from temp array 

import random
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array
        

    def shuffle(self):
        tmp = list(self.array)
        
        for i in range(len(self.array)):
            removed_idx = random.randrange(len(tmp))
            self.array[i] = tmp.pop(removed_idx)
        return self.array
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
