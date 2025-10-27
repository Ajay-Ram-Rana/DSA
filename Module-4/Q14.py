def nextPermutation(A):
  n  = len(A)
  i = n-2
  while i>=0 and A[i]>=A[i+1]:
    i=i-1
  if i==-1:
    return A[::-1]
  j = n-1
  while i<=j and A[i]>=A[j]:
    j = j-1
  A[i],A[j] = A[j],A[i]
  A[i+1:n] = A[i+1:n][::-1]

  return A    
 

def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A = list(map(int,input("A: => ").split()))
    B = nextPermutation(A)
    print(f"Next Permutation : => {B}")
    n  = n-1


if __name__ =="__main__":
  main()