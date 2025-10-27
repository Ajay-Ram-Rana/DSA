def toggle_case(A):
  for i in A:
    if i.islower():
      A = A.replace(i,i.upper())
    else:
      A = A.replace(i,i.lower())

  return A      



def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A = input("String:")
    B = toggle_case(A)
    print(f"Toggle case: {B}")


    n  = n-1

if __name__ == "__main__":
  main()