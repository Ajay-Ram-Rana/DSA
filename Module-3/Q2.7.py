def count_increasing_triplet(A):
  n = len(A)
  if n<3:
    return 0
  
  count = 0
  for i in range(n-2):
    if A[i]<A[i+1]<A[i+2]:
      count = count+1
  return count



def main():
  n  = int(input("How many inputs:"))
  while n>0:
    A = list(map(int,input().split()))
    x = count_increasing_triplet(A)
    print(f"Total Increasing Triplets : {x}")
    n = n-1


if __name__ == "__main__":
  main()