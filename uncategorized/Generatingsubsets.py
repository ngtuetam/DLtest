def GenerateSubset(k) :
    if (k>n) : 
        # Process the subset
        print("[ "+' '.join ( map (str,subset) ) + " ]")
    else :
        # Generate subset with k
        subset.append(k)
        GenerateSubset (k + 1)

        # Generate subset without k
        subset.pop()
        GenerateSubset (k + 1)
k = 1 
subset = []
n = int(input())
GenerateSubset(k) 
