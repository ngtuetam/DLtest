#leetcode: Roman to Integer
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        res += d[s[0]]
        for i in range(1,len(s)):
            if d[s[i]] > d[s[i-1]]:
                res += d[s[i]] - 2*d[s[i-1]]
            else:
                res += d[s[i]]
        return res