# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
# Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
# Output: false
class Solution:
    def isRectangleOverlap(self, rec1, rec2 ) -> bool:
        # no overlap
        if rec1[1] >= rec2[3] or rec1[3] <= rec2[1] or rec1[0] >= rec2[2] or rec1[2] <= rec2[0]:
            return False
        return True