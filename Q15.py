def prefix_sum(A):
  arr = []
  sum = 0
  for i in range(len(A)):
    sum = sum+A[i]
    arr.append(sum)

  return arr  



def main():
  n = int(input("How many Inputs:"))
  while n>0:
    A  = list(map(int,input("Array A:").split()))
    B  = prefix_sum(A)
    print(B)
    n = n-1




if __name__ == "__main__":
  main()