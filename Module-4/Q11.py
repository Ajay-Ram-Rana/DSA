def trap(A):
  n  = len(A)
  if n==0:
    return 0
  left_max = [0]*n
  right_max = [0]*n
  ans = 0
  left_max[0] =  A[0]
  for i in range(1,n):
    left_max[i]  =  max(left_max[i-1],A[i])

  right_max[n-1] = A[n-1]
  for j in range(n-2,-1,-1):
    right_max[j] = max(right_max[j+1],A[j])

  for k in range(n):
    ans = ans+min(left_max[k],right_max[k])-A[k]

  return ans       


def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    A = list(map(int,input("A: ").split()))
    x  = trap(A)
    print(f"Total traped in Water : {x}")
    n = n-1

if __name__ == "__main__":
  main()