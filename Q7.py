def occurance(A,B):
  count = 0
  n = len(A)
  for num in A:
    if num == B:
      count = count+1
  return count    

def main():
  n = int(input("How many Inputs:"))
  while n>0:
    A = list(map(int,input("Array: ").split()))
    B = int(input("Integers : "))
    times = occurance(A,B)
    print(f"{B} occur in Array{A} => {times} times ")
    n = n-1 



if __name__ =="__main__":
  main()