def Fi(n):
  if(n<=1):
    return n
  return Fi(n-1) + Fi(n-2) 
