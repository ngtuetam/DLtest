#220829
# https://leetcode.com/problems/maximum-subarray/
# Kadane’s Algorithm:

def maxSubArraySum(a,size):
       
    max_so_far = -100000000 - 1
    max_ending_here = 0
       
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
  
        if max_ending_here < 0:
            max_ending_here = 0   
    return max_so_far
   
# Driver function to check the above function 
  
a = [-2, -3, -4, -5, -10, -1, -5, -3]
  
print(maxSubArraySum(a,len(a)))



