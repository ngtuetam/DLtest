def common_element(list1, list2):
    n = len(list1)
    m = {}
    ans = []
    for i in range(n):
        m[list1[i]] = i
    for i in range(n):
        if list2[i] in m:
            ans.append(list2[i])
    if ans:
        return ans
    return False

list1 = [2,3,4]
list2 = [5,5,5]
print(common_element(list1,list2))

