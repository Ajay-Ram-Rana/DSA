def reverse_string(A):
  n  = len(A)
  result =""
  while n>0:
    result = result+A[n-1]
    n = n-1
  return result  



def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    A = input("String: ")
    B = reverse_string(A)
    print(f"Reversed: {B}") 
    n = n-1


if __name__ == "__main__":
  main()