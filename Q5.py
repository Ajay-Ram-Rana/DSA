def equal_array(A,max):
  n = len(A)
  time = 0
  for i in range(n):
    if A[i]!=max:
      time = time+max-A[i]
  return time     



def to_make_equal_array(A):
  n  = len(A)
  i = 0
  while i+1<n:
    if A[i]>A[i+1]:
      max = A[i]
    else:
      max = A[i+1]
    i=i+1    
  
  return equal_array(A, max)   


def main():
  n  = int(input("How many Inputs:"))
  while n>0:
    A = list(map(int,input("Array: ").split()))
    time = to_make_equal_array(A)
    print(f"To make equal all the elements of given array:::Time taken(in sec)=>{time}")
    n=n-1



if __name__ =="__main__":
  main()