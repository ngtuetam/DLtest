#P: Given a set,generate all possible subset of size n of given set within a list.

#Input : {1, 2, 3, 4}, n = 3
#Output : [{1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4}]

import itertools
def findsubsets(s, n):
    return list(itertools.combinations(s, n))
# Driver Code
s = {1, 2, 3}
n = 2
print(findsubsets(s, n))

