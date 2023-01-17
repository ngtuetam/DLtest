# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
l = list(map(int, (input().split())))
l.sort()
mean = 0
sum = 0
median = 0
max_count = 1
mode = l[0]
cur_count = 1
for i in l:
    sum += i
mean = sum / n

if n %2 == 1:
    median = l[n//2]
else:
    median = (l[n//2 ] + l[n//2 +1]) / 2
    
for i in range(n-1):
    if l[i] == l[i+1]:
        cur_count += 1
    else:
        max_count = 1
    if cur_count > max_count:
        max_count = cur_count
        mode = l[i+1]
    
        

print(mean)
print(median)
print(mode)