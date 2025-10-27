def Amazing_subarray(A):
  vowels = "aeiouAEIOU"
  count =0
  mod  = 10003
  n = len(A)
  for i in range(n):
    if A[i] in vowels:
      count = count+(n-i)
      count = count % mod
  return count    


def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A = input("String: ")
    m = Amazing_subarray(A)
    print(f"# of Amazing Subarray: {m}")

    n = n-1



if __name__ == "__main__":
  main()