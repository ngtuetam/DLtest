# Count Square Sum Triples
class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        l = [i*i for i in range(1,n+1)]
        for i in range(n-1,1,-1):
            a = 0
            b = i-1
            while a<=b:
                if l[a] + l[b] > l[i]:
                    b-=1
                elif l[a] + l[b] < l[i] :
                    a+=1
                else:
                    cnt+=1
                    a+=1
        return cnt*2

# def countTriples(n: int):
#     cnt = 0
#         l = [i for i in range(1,n+1)]
#         res = []
#         for i in range(n-1,1,-1):
#             a = 0
#             b = i-1
#             while a<=b:
#                 if l[a]**2 + l[b]**2 > l[i]**2:
#                     b-=1
#                 elif l[a]**2 + l[b]**2 < l[i]**2 :
#                     a+=1
#                 else:
#                     res.append([l[a],l[b],l[i]])
#                     res.append([l[b],l[a],l[i]])
#                     cnt+=1
#                     a+=1
#     return res
