def factorial(A):
  if A<=1:
    return 1
  ans  = factorial(A-1)*A
  return ans



def main():
  n  = int(input("How many inputs:"))
  while n>0:
    A  = int(input("N:=> any +ve integer::=> "))
    B  = factorial(A)
    print(f"Factorial({A}) = {B}")
    n  = n-1


if __name__ == "__main__":
  main()