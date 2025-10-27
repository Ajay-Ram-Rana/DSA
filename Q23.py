def sum_subarray(A):
  #final  = []
  n  = len(A)
  
  final_sum  = 0
  for i in range(n):
    #current = []
    sum  = 0
    for j in range(i,n):
      #current.append(A[j])
      sum = sum+A[j]
      #final.append(current.copy())
      final_sum = final_sum + sum

  return final_sum  




def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    A = list(map(int,input("Array A :=> ").split()))
    sum = sum_subarray(A)
    print(f"Sum of all subarrays of given Array : => {sum}")
    n=n-1



if __name__=="__main__":
  main()