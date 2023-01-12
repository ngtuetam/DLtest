def merge(intervals):
    n = len(intervals)
    intervals.sort()
    i = 1
    if n == 1:
        return intervals
    # if n == 2 and (intervals[0][0] > intervals[1][0] or intervals[1][0] > intervals[0][1]):
    #     return intervals
    res = [intervals[0]]
    for i in range(1,n):
        check = res[-1]
        if check[0] <= intervals[i][0] <= check[1]:
            res.pop()
            res.append([check[0],max(intervals[i][1],check[1])])
        else:
            res.append(intervals[i])
    return res



# intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[0 ,2], [1 ,4], [3, 5]]
print(merge(intervals))


# 0 2, 1 4, 3 5


# i = 0, j = 1