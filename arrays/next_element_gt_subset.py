# hashmap + 0(n*m)
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = [-1]*len(nums1)
        hashmap = {}
        flag = False
        for i in range(len(nums1)):
            hashmap[nums1[i]] = i
        for i in range(len(nums2)):
            if nums2[i] not in hashmap:
                continue
            for j in range(i+1,len(nums2)):
                if nums2[j] > nums2[i]:
                    indx = hashmap[nums2[i]]
                    res[indx] = nums2[j]
                    break
        return res