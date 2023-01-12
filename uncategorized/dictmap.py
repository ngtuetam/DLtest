'''
https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem?isFullScreen=true
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = value
    
while True:
    try:
        n = input()
        if n in d:
            print(n+"="+d[n])
        else:
            print("Not found")
    except EOFError:
        break
        
    