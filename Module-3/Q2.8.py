def palindrome(A):
  B  = list(A)
  n  = len(B)
  for i in range(n):
    if B[i]!=B[n-1-i]:
      return False
  return True


def main():
  n = int(input("How many inputs:"))
  while n>0:
    A  = input("String: ")
    B = palindrome(A)
    print(f"{A} is Palindrome : {B}")
    n = n-1


if __name__ == "__main__":
  main()