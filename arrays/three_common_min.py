'''
Find the Smallest Common Number
Given three integer arrays sorted in ascending order, return the smallest number found in all three arrays.
Input: 
ar1[] = {1, 5, 10, 20, 40, 80} 
ar2[] = {6, 7, 20, 80, 100} 
ar3[] = {3, 4, 15, 20, 30, 70, 80, 120} 
Output: 20, 80

Input: 
ar1[] = {1, 5, 5} 
ar2[] = {3, 4, 5, 5, 10} 
ar3[] = {5, 5, 10, 20} 
Output: 5, 5
'''
def smallest_common(nums1, nums2, nums3):
    n1 = len(nums1)
    n2 = len(nums2)
    n3 = len(nums3)
    i = j = k = 0
    res = []
    while i < n1 and j < n2 and k < n3:
        if nums1[i] == nums2[j] and nums2[j] == nums3[k]:
            # res.append(nums1[i])
            return nums1[i]
            # i += 1
            # j+=1
            # k +=1

        elif nums1[i] < nums2[j]:
            i += 1
        elif nums2[j] < nums3[k]:
            j+=1
        else:
            k += 1
    # return res[0]
    return -1


ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
print(smallest_common(ar1,ar2,ar3))