def greater(A):
  n  = len(A)
  numbers = 0
  prev = float('-inf')
  for num in A:
    num_count = 0
    for m in A:
      if m > num:
        num_count = num_count+1
    if num_count!=0:
      numbers = numbers+1
  return numbers      





def main():
  n  = int(input("How many Inputs:"))
  while n>0:
    A = list(map(int,input("Array: ").split()))
    B  = greater(A)
    print(f"Number of elements in given array having at least 1 greater element::: {B}")
    n = n-1


if __name__ == "__main__":
  main()