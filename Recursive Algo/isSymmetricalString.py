'''Problem: Một chuỗi s có độ dài nn bao gồm các kí tự in hoa, thường và chữ số. Kiểm tra xem chuỗi s có phải là chuỗi đối xứng không.
Solution: De quy : Kiem tra tuan tu ki tu i va n-i-1
             - Base case : Neu i>= j : tra ve True/False
             - Nguoc lai :- Neu ki tu i = ki tu j (j = n-i-1) : kiem tra ki tu i+1 va j-1
                          - Nguoc lai : Tra ve True/False
ĐPT : O(n/2)                     
'''
import sys
sys.setrecursionlimit(10**6)

def isSymmetric(s, i, j):
  if i >= j:
    return True
  if s[i] == s[j]:
    return isSymmetric(s, i + 1, j - 1)
  return False
  
  
n = int(input())
s = input()
if (isSymmetric(s, 0, n - 1)):
  print('YES')
else:
  print('NO')
