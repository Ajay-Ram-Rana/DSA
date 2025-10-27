def min_xor(A):
  A.sort()
  min_xor_value = float('inf')
  n  = len(A)
  for i in range(n-1):
    xor_value = A[i]^A[i+1]
    if xor_value < min_xor_value:
      min_xor_value = xor_value
  return min_xor_value    


def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A = list(map(int,input("A: => ").split()))
    B = min_xor(A)
    print(f"Minimum Xor Value: {B}")
    n  = n-1


if __name__ == "__main__":
  main()