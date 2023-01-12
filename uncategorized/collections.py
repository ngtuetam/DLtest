# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
'''
from collections import Counter
x = int(input())
shoe_size = Counter(list(map(int,input().split())))
n = int(input())
res = 0

for _ in range(n):
    size, price = input().split()
    if int(size) in shoe_size.keys() and shoe_size[int(size)] != 0:
        res += int(price)
        shoe_size[int(size)] -= 1

print(res)