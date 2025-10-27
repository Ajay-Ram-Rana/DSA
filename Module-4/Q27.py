def no_subarray_with_OR_1(A):
  n  = len(A)
  total_subarray = n*(n+1)//2
  zeros_subarray = 0
  count = 0
  for num in A:
    if num ==0:
      count = count+1
    else:
      zeros_subarray = zeros_subarray + count*(count+1)//2
      count = 0 
  zeros_subarray = zeros_subarray + count*(count+1)//2

  return total_subarray-zeros_subarray     


def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    A = list(map(int,input("A::=> only 1's & 0's :: ").split()))
    B = no_subarray_with_OR_1(A)
    print(f"Total Subarray with OR = 1: => {B}")
    n  = n-1

if __name__ == "__main__":
  main()