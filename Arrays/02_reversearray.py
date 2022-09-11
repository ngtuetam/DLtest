#220829
#Problem: https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

from os import TMP_MAX


def reverse_list(arr, start, end):
    tmp = 0
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start +=1
        end -=1
    return arr

A = [1, 2, 3, 4, 5, 6]
print(A)
reverse_list(A, 0, 5)
print("Reversed list is")
print(A)   #A[::-1]