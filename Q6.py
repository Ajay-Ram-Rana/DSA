def second_largest(A):
  n  = len(A)
  if n<2:
    return -1 
  
  largest = second_max = float('-inf')

  for num in A:
    if num>largest:
      second_max = largest
      largest = num
    elif largest>num>second_max:
      second_max = num

  return second_max if second_max != float('-inf') else -1    





def main():
  n  = int(input("How many inputs:"))
  while n>0:
    A = list(map(int,input("Array: ").split()))
    second_max  = second_largest(A)
    print(f"Second Largest Element ::: {second_max} ")
    n = n-1

if __name__ =="__main__":
  main()