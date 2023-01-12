#220829
#recur for max and min of left half and right half

class pair:
    def __init__(self):
        self.min = 0
        self.max = 0

def getMinMax(low, high, arr):
    arr_max = arr[low]
    arr_min = arr[low]

    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_max, arr_min)

    elif high == low + 1:
        if arr[0] > arr[1]:
            arr_max = arr[0]
            arr_min = arr[1]
        else:
            arr_max = arr[1]
            arr_min = arr[0]
        return (arr_max, arr_min)
    else:
        mid = int((low + high ) / 2)
        arr_max1, arr_min1 = getMinMax(low, mid, arr)
        arr_max2, arr_min2 = getMinMax(mid +1, high, arr)
        return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
arr_max, arr_min = getMinMax(low, high, arr)
print('Minimum element is ', arr_min)
print('Maximum element is ', arr_max)
