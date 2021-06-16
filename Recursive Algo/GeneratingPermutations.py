#If ‘n’ is the number of distinct items in a set, the number of permutations is n!
def Generate(per,ele,pos):
    
   if( len(per) == len(ele) ):
        for item in per:
          print(item, end=' ')
        print('\n')

   else:

       for i in range (0, len(ele)):

           if (pos[i]):
               continue

           pos[i] = True
           per.append(ele[i])

           Generate (per,ele,pos)
  
           per.pop()
           pos[i] = False
           

ele = []
per = []
size = int(input())
for i in range(0, int(size)):
   x = int(input())
   ele.append(x)

pos = [False] * int(size)

print("\nPermutations\n")
Generate(per, ele, pos)

  
