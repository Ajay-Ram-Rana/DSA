def min_swap(A,B):
  n  = len(A)
  if n==0:
    return 0
  
  countGood = sum(1 for i in A if i<=B)
  if countGood ==0:
    return 0
  
  currentGood  = sum(1 for x in A[:countGood] if x<=B)
  maxGood = currentGood

  for i in range(countGood,n):
    if A[i]<=B:
      currentGood = currentGood+1
    if A[i-countGood]<=B:
      currentGood = currentGood -1
    if currentGood>maxGood:
      maxGood = currentGood
  return countGood - maxGood        


def main():
  n  = int(input("How many inputs:"))
  while n>0:
    A = list(map(int,input("Array: ").split()))
    B = int(input("B:=> ")) 
    x = min_swap(A,B)
    print(f"Minimum Swap to be together all numbers <= {B}: ==> {x}")
    n = n-1


if __name__ == "__main__":
  main()