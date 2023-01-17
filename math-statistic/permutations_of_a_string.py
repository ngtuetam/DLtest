# Print all permutations of a given string.
# recursion and backtracking

def to_string(list):
    return ''.join(list)

def permute(list, l, r):
    if l == r:
        print(to_string(list))
    else:
        for i in range(l,r):
            list[l], list[i] = list[i], list[l]
            permute(list,l+1,r)
            list[l], list[i] = list[i], list[l]

string = "ABC"
n = len(string)
a = list(string)
 
# Function call
permute(a, 0, n)