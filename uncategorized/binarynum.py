'''
https://www.hackerrank.com/challenges/30-binary-numbers/problem?isFullScreen=true
'''
#!/bin/python3
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    bit = []
    while n:
        bit.append(n%2)
        n = n//2
    bit = bit[::-1]
    m = 0
    cnt =0
    for i in range(len(bit)):
        if bit[i] == 0:
            cnt = 0
        else:
            cnt+=1
            m = max(m, cnt)
    print(m)