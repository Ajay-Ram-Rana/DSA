
def rangeSum(A,B):
  arr = []
  for pair in B:
    sum = 0
    for idx in range(pair[0],pair[1]+1):
      sum  = sum + A[idx]     
    arr.append(sum)
  return arr  
    
  
 


def main():
  n  = int(input("How many Inputs : "))
  while n>0:
    A  = list(map(int , input("Array A:=> ").split()))
    B_input = input("Array B (pairs separated by ';'):=> ").split(';')
    B = [list(map(int, pair.split())) for pair in B_input]
    C = rangeSum(A,B)
    print(f"Output Array: => {C}")
    n=n-1



if __name__ == "__main__":
  main()