def max_subarray_sum(A,B):
  n  = len(A)
  if B>n or n ==0:
    return -1
  
  window_sum = sum(A[:B])
  max_sum = window_sum
  for i in range(B,n):
    window_sum = window_sum + A[i] -A[i-B]
    max_sum = max(window_sum,max_sum)
  return max_sum   



def main():
  n  = int(input("How many Inputs:"))
  while n>0:
    A  = list(map(int,input("A: => ").split()))
    B  = int(input("B:(Size of Subarray:)"))
    m  = max_subarray_sum(A,B)
    print(f"Max Subarray Sum of {B} length :=> {m}")
    n = n-1


if __name__ == "__main__":
  main()