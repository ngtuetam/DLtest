# 0 + 0 = 0
# 0 + 1 = 1
# 1 + 0 = 1
# 1 + 1 = 10
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
 
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        res = ""
        carry = 0
        for i in range(max_len - 1, -1, -1):
            r = carry
            if a[i] == '1': 
                r += 1
            if b[i] == '1':
                r+= 1
            if r % 2 == 1:
                res = '1' + res
            else:
                res = '0' + res
            carry = 0 if r < 2 else 1
        if carry:
            res = '1' + res
        return res   