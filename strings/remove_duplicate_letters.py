#leetcode : Remove Duplicate Letters
# Input: s = "bcabc"
# Output: "abc"
# Input: s = "bcab"
# Output: "bca"

def remove_dup(s):
    count = {}
    vis = set()
    st = []

    for c in s:
        if c not in count:
            count[c] = 0
        count[c] +=1
    
    for c in s:
        if c not in vis:
            while st and st[-1] > c and count[st[-1]] > 0:
                vis.remove(st.pop())
            st.append(c)
            vis.add(c)
        count[c] -=1
    st = ''.join(st)
    return st


s = "bcabc"
print(remove_dup(s))