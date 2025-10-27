def min_max_subarray(A):
  n = len(A)
  minVal = min(A)
  maxVal = max(A)
  if minVal==maxVal:
    return 1
  
  lastMin = -1
  lastMax = -1
  minLen = n


  for i in range(n):
    if A[i] ==minVal:
      lastMin = i
      if lastMax !=-1:
        minLen = min(minLen , i-lastMax+1)
    if A[i] ==maxVal:
      lastMax = i
      if lastMin!=-1:
        minLen = min(minLen,i-lastMin+1)

  return minLen        



def main():
  n = int(input("How many inputs:"))
  while n>0:
    A = list(map(int,input("Array A:=> ").split()))
    m  = min_max_subarray(A)
    print(f"No of Subarray , min max occurrance at least one: =>{m}")
    n= n-1



if __name__ == "__main__":
  main()