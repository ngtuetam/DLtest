# leetcode: Add Strings
# Input: num1 = "11", num2 = "123"
# Output: "134"

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = ""
        carry = 0
        if len(num1) < len(num2):
            for _ in range(len(num2)-len(num1)):
                num1 += '0'
        elif len(num1) > len(num2):
            for _ in range(len(num1)-len(num2)):
                num2 += '0'
        for i in range(len(num1)):
            s = (ord(num1[i])-48) + (ord(num2[i])-48)
            s_ = (s + carry)%10
            carry =  (s + carry) // 10
            ans += str(s_)
        if carry:
            ans += str(carry)
        ans = ans[::-1]
        return ans



