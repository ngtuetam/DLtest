'''
Problem: 1343B
Solution : le + le = chan -> nua chan va nua le phai chan -> n chia het cho 4
VD: Cho n = 8 : 2,4,6,8,1,3,5,x
2,4,5,8,2-1,4-1,6-1,x
Chia thanh hai phan chan le
2,4,...,n,2-1,4-1,...,x
Tong nua chan : (2+4+...+n)
Tong nua le : (2-1+4-1+...+x)
->  (2+4+...+n) = (2-1+4-1+...+x)
    (2+4+...+n) = (2+4+...+x)- 1*(n/2 -1)
    n = x - n/2 +1
    x = 3n/2 -1 
    Dat n = n//2
    x = 3n-1
-> n = 8, x=11
'''
t = int(input())
for _ in range(t):
	n = int(input())
	if n%4 != 0:
		print("NO")
	else:
		n=n//2
		print("YES")
		for i in range(1,n+1):
			print(i*2,end=" ")
		for i in range(1,n):
			print(i*2-1,end =" ")
		print(3*n-1)
