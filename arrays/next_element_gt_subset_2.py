# hashmap + stack + o(m+n)
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = [-1]*len(nums1)
        hashmap = {}
        st = []
        for i in range(len(nums1)):
            hashmap[nums1[i]] = i
        for i in range(len(nums2)):
            cur = nums2[i]
            while st and cur > st[-1]:
                val = st.pop()
                indx = hashmap[val]
                res[indx] = cur
            if cur in hashmap:
                st.append(cur)

        return res
