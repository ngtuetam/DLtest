def merge(intervals):
    intervals.sort()
    res = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnd = res[-1][1]

        if start <= lastEnd:
            res[-1][1] =  max(end, lastEnd)
        else:
            res.append([start,end])
    return res


intervals = [[0 ,2], [1 ,4], [3, 5]]
print(merge(intervals))