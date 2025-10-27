def fibonacci(A):
  if A<=1:
    return A 
  ans = fibonacci(A-2)+fibonacci(A-1)
  return ans


def main():
  n  = int(input("How many inputs:"))
  while n>0:
    A  = int(input("N: (Fibonacci Series Nth: )"))
    B = fibonacci(A)
    print(f"{A}th fibonacci Number::=> {B}")
    n  = n-1


if __name__ == "__main__":
  main()

