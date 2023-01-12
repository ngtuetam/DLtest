# sorting by random index
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
        for i in range(len(self.array)):
            random_indx = random.randrange(len(self.array))
            self.array[i], self.array[random_indx] = self.array[random_indx], self.array[i]
        return self.array

        
# this address is located

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()