def no_subarray(A,B):
  n  = len(A)
  if n==0:
    return 0
  
  count = 0
  curr_sum = 0
  left = 0

  for right in range(n):
    curr_sum = curr_sum + A[right]

    while curr_sum>=B and left<=right:
      curr_sum  =  curr_sum - A[left]
      left = left+1
    count = count+(right-left+1)

  return count    






def main():
  n = int(input("How many inputs: "))
  while n>0:
    A = list(map(int,input("A: => ").split()))
    B = int(input("B:=>"))
    m = no_subarray(A,B)
    print(f"No of Subarray contained the sum less than {B}:==> {m}")
    n=n-1


if __name__ == "__main__":
  main()