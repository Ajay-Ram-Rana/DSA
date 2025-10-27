def subarray_count(A,B,C):
  n  = len(A)
  if n==0 or B<=0  or B>n:
    return 0
  
  current_sum  = sum(A[:B])
  if current_sum == C:
    return 1
    
 
  for i in range(B,n):
    current_sum = current_sum + A[i] - A[i-B]
    if current_sum == C:
      return 1
    

  return 0        
        
        
   


def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    A = list(map(int, input("A : => ").split()))
    B = int(input("B:(length of subarray ) => "))
    C = int(input("C: Sum of the subarray: => "))
    m  = subarray_count(A,B,C)  
    print(f"Total number of subarray of length {B} with sum {C} : => {m}")
    n=n-1


if __name__ == "__main__":
  main()