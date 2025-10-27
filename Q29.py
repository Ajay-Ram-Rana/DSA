def subarray_least_average(A,B):
  n  = len(A)
  if B>n or n==0:
    return -1
  
  curr_sum = sum(A[:B])
  least_sum = curr_sum
  start_index = 0 

  for i in range(B,n):
    curr_sum = curr_sum + A[i] - A[i-B]
    if curr_sum<least_sum:
      least_sum = curr_sum
      start_index = i-B+1

  return start_index     
    




def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A = list(map(int,input("A:=> ").split()))
    B = int(input("B :(Size of subarray)=> "))
    m = subarray_least_average(A,B)
    print(f"Least Average of {B} size subarray of array {A}:=>  {m}")
    n=n-1


if __name__ == "__main__":
  main()