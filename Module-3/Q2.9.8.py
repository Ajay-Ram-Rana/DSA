def reverse_strings(A):
  words = A.strip().split()
  words.reverse()
  return " ".join(words)





def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    A = input("List of string:")
    B = reverse_strings(A)
    print(f"After Reverse : {B}")
   
    n  = n-1


if __name__ =="__main__":
  main()