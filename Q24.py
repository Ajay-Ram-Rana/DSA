def sum_subarray(A):
  #final  = []
  n  = len(A)
  
  total  = 0
  for i in range(n):
    total = total+A[i]*(i+1)*(n-i)

  return total  




def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    A = list(map(int,input("Array A :=> ").split()))
    sum = sum_subarray(A)
    print(f"Sum of all subarrays of given Array : => {sum}")
    n=n-1



if __name__=="__main__":
  main()