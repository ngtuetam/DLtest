# 220829
# Problem : https://www.geeksforgeeks.org/chocolate-distribution-problem/

def find_min_diff(arr, n, m):
    if (m==0 or n==0):
        return 0
    arr = sorted(arr)

    if m > n:
        return -1

    min_diff = 100000000
    for i in range(n-m+1):
        if arr[m+i-1] - arr[i] <= min_diff:
            min_diff = arr[m+i-1] - arr[i]

    return min_diff

if __name__ == "__main__":
    arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
    n = len(arr)
    m = 7  
    print("Minimum difference is", find_min_diff(arr, n, m))
    