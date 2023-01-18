# leetcode: Reverse Words in a String
# Input: s = "the sky is blue"
# Output: "blue is sky the"
# The “Hello World” string should be reversed as “World Hello”.
# The quick brown fox jumped over the lazy dog.
# -> dog. lazy the over jumped fox brown quick The


def reverseWords(s):
    l = s.split()
    n = len(l)-1
    res = " "
    while n>=0:
        res += " "+l[n]
        n -=1
    res = res.strip()
    return res
 
# Driver Code
s = "The quick brown fox jumped over the lazy dog."
 
# Function call
print(reverseWords(s))