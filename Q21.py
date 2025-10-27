def max_possible_sum(A,B):
  n  = len(A)

  left = [0]*(B+1)
  for i in range(1,B+1):
    left[i] = left[i-1]+A[i-1]

  right = [0]*(B+1)
  for j in range(1,B+1):
    right[j] = right[j-1] + A[n-j]

  max_sum = float('-inf')
  for k in range(B+1):
    total = left[k] + right[B-k]
    if total>max_sum:
      max_sum = total

  return max_sum     




def main():
  n  =int(input("How many inputs:"))
  while n>0:
    A  = list(map(int,input("Array A:=> ").split()))
    B = int(input("Integer: "))
    m = max_possible_sum(A,B)
    print(f"Maximum Possible Sum  => {m}")
    n=n-1



if __name__ =="__main__":
  main()