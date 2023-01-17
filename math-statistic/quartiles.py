#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr.sort()
    n = len(arr)      
    m = n //2
    l = m//2
    r= n-l
    if m % 2==0:
        l=(arr[l-1]+arr[l])//2
        r=(arr[r-1]+arr[r])/2         
    else :
        l=arr[l]    
        r= arr[r-1]
    if n % 2==0:
        m=(arr[m-1]+arr[m])//2             
    else:
        m=arr[m] 
    m = int(m)
    r = int(r)
    l = int(l)    
    return l,m,r             

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()