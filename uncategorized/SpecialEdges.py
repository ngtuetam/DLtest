'''
Problem: Cho đồ thị có hướng được biểu diễn bằng danh sách cạnh (edge list). 
Trong đồ thị có các cạnh khuyên. Hãy đếm số lượng khuyên và tính tích trọng số các cạnh khuyên đó
Do tích các cạnh khuyên có thể rất lớn, ta chỉ cần in số dư của kết quả khi chia cho 10^{6} + 7

Solution : - Doc vao danh sach cac canh cua do thi (edge_list). Moi canh luu trong cau truc Edge
           - count: dem so luong cac canh khuyen, ban dau bang 0 
           - ans: tich cac canh khuyen, ban dau bang 1 
           - Duyet dsach edge_list,neu canh nao co 2 dinh trung nhau -> cap nhat so luong va tich cac canh khuyen hien tai.
           - TH so luong canh khuyen = 0 -> in -1
'''
#code
class Edge:  
    def __init__(self, u, v, w):  
        self.u = u  
        self.v = v  
        self.w = w  
  
m = int(input())  
  
edge_list = []  
for i in range(m):  
    u, v, w = map(int, input().split())  
    edge_list.append(Edge(u, v, w))  
       
count = 0  
ans = 1  
  
for edge in edge_list:  
    if edge.u == edge.v:  
        count += 1  
        ans = (ans * edge.w) % 1000007  
  
if count > 0:  
    print(count, ans)
else:  
    print(-1)
