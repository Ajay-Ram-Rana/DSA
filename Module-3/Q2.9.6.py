def occurance(A):
  s = "bob"
  n  = len(A)
  if n==0:
    return ""
  count = 0
  for i in range(n-2):
    if A[i:i+3] == s:
      count = count+1
  return count


def main():
  x = "bob"
  n  = int(input("How many Inputs: "))
  while n>0:
    A = input("String: ")
    m = occurance(A)
    print(f"Occurance of {x} in given String  => {m}")
    n = n-1



if __name__ =="__main__":
  main()