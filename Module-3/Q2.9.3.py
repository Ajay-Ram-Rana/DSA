def longest_common_prefix(A):
  n  =len(A[0])
  prefix  = ""
  first_word = A[0]
  for i in range(n):
    ch = first_word[i]
    for word in A[1:]:
      if i>=len(word) or  word[i] != ch:
        return prefix
    prefix = prefix+ch
  return prefix    
      



def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A = input("Strings list: ").split()
    B = longest_common_prefix(A)
    print(f"Longest  Common Prefix : {B} ")
    n = n-1


if __name__ =="__main__":
  main()