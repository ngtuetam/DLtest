# leetcode: Reverse Words in a String
# Input: s = "the sky is blue"
# Output: "blue is sky the"
# The “Hello World” string should be reversed as “World Hello”.
# The quick brown fox jumped over the lazy dog.
# -> dog. lazy the over jumped fox brown quick The


def reverseWords(s):
    n = len(s)
    i = 0
    j = 0
    res = ""
    while True:
        while i < n and s[i] == ' ':
            i +=1
        if i == n:
            break
        j = i+1
        while j<n and s[j] != ' ':
            j+=1

        sub = s[i:j]
        if len(res) == 0:
            res = sub
        else:
            res = sub + " " + res

        i = j

    return res


# Driver Code
s = "hello world."
 
# Function call
print(reverseWords(s))




 
