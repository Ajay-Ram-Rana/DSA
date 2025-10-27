def max_sum(A):

  curr_sum = A[0]
  max_sum = A[0]
  
  if not A:
    return 0
  for i in range(1,len(A)):
    curr_sum = max(A[i], curr_sum+A[i])
    max_sum = max(curr_sum,max_sum)
  return max_sum

  




def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A = list(map(int,input("Array: ").split()))
    x = max_sum(A)
    print(f"Maximum Sum => {x}")


    n  = n-1


if __name__ =="__main__":
  main()