def nobel_integer(A):
  n = len(A)
  if n==0:
    return -1
  A.sort()
  if n==1:
    return 1 if A[0]==0 else -1
  
  count = 0
  for i in range(1,n):
    if (A[i]==(n-i-1)) and (A[i]!=A[i-1]):
      count = count+1
  if count!=0:
    return 1
  else:
    return -1    

    


def main():
  n  = int(input("How many inputs:"))
  while n>0:
    A = list(map(int,input("A:").split()))
    m = nobel_integer(A)
    print(f"Nobel integers are there if return the value 1 else -1: => {m}")
    n = n-1



if __name__ =="__main__":
  main()