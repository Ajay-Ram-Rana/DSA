def A_P(A):
  n  = len(A)
  if n==0 or n==1:
    return 0
  A.sort()
  common_difference  = A[1]-A[0]
  current_difference = common_difference 
  for i in range(1,n):
    current_difference = A[i] - A[i-1]
    if current_difference != common_difference:
      return 0
      break
  return 1
  
    


def main():
  n  = int(input("How many Input:"))
  while n>0:
    A = list(map(int,input("A: ").split()))
    m  = A_P(A)
    print(f"Given Array can be formed AP then return 1 else 0: => {m}")
    n = n-1


if __name__ =="__main__":
  main()