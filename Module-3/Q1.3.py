def min_cost(A):
  n  = len(A)
  
  if n==0:
    return 0
  if n==1:
    return A[0]
  
  A.sort()

  total_cost = 0
  current_sum = sum(A)
  for i in range(n):
    total_cost = total_cost+current_sum
    current_sum = current_sum-A[-1-i]
  return total_cost  

def main():
  n = int(input("How many input:"))
  while n>0:
    A = list(map(int,input("A: => ").split()))
    m = min_cost(A)
    print(f"Minimum Cost of the given array : => {m}")
    n =  n-1


if __name__ =="__main__":
  main()