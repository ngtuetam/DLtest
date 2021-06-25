'''Problem: Đếm số lượng các phần tử giá trị "Hoàng Hậu" trên ma trận vuông (nxn)
         Một giá trị được gọi là Hoàng Hậu khi nó là giá trị lớn nhất trên dòng, trên cột và hai đường chéo đi qua nó.
 '''
'''Solution:    
 - Ham ismaxDirection(a,n,col,row,x,y) x,y la buoc nhay de kiem tra phan tu lon nhat tren dg cheo
 - Ham isQueen(a,n,row,col)
    + Ktra ptu lon nhat tren hang
    + Ktra ptu lon nhat tren cot
    + Ktra theo 4 huong: 
      > Huong tu duoi len goc trai tren (i-1, j-1), buoc nhay (-1,-1)
      > Huong tu tren xuong goc trai duoi (i+1, j-1) , buoc nhay (1,-1)
      > Huong tu duoi len goc phai tren (i-1, j+1) , buoc nhay (-1,1)
      > Huong tu tren xuong goc phai duoi (i+1, j+1), buoc nhay (-1,-1)
'''
#Code:
def ismaxDirection(a,n,row,col,x,y):
	i = row
	j = col
	while 0<= i <n and 0<= j <n:
		if a[i][j] > a[row][col]:
			return False
		i+=x
		j+=y
	return True
def isQueen(a,n,row,col):
	#Kiem tra phan tu lon nhat tren hang
	for j in range(n):
		if a[row][j] > a[row][col]:
			return False
	#Kiem tra phan tu lon nhat tren cot
	for i in range(n):
		if a[i][col] > a[row][col]:
			return False
	#Kiem tra theo 4 huong
	dr1 = ismaxDirection(a,n,row,col,-1,-1)
	dr2 = ismaxDirection(a,n,row,col,-1,1)
	dr3 = ismaxDirection(a,n,row,col,1,-1)
	dr4 = ismaxDirection(a,n,row,col,1,1)
	return dr1 and dr2 and dr3 and dr4

n = int(input())
a = []
for i in range(n):
	t = list(map(int,input().split()))
	a.append(t)
count = 0
for i in range(n):
	for j in range(n):
		if isQueen(a,n,i,j):
			count+=1
print(count)
