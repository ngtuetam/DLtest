def common_element(list1, list2):
    n = len(list1)
    m = {}
    ans = []
    for i in range(n):
        m[list1[i]] = True
    for i in range(n):
        if list2[i] in m:
            return True
    return False

list1 = [2,3,4]
list2 = [5,4,5]
print(common_element(list1,list2))

