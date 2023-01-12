# 220829 
# Problem: https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

class Pair:
    def __init__(self):
        self.min = 0
        self.max = 0
    
def getMinMax(arr: list, n: int) -> Pair:
    minmax = Pair()

    if n == 1:
        minmax.min = arr[0]
        minmax.max = arr[0]

    if arr[0] > arr[1]:
        minmax.min = arr[1]
        minmax.max = arr[0]
    else:
        minmax.min = arr[0]
        minmax.min = arr[1]
    
    for i in range(2,n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.max:
            minmax.min = arr[i]

    return minmax
    

if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = 6
    minmax = getMinMax(arr, arr_size)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)