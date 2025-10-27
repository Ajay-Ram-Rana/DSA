def anagrams(A,B):
  if len(A)!=len(B):
    return 0
  freq = [0]*26
  for  ch in A:
    freq[ord(ch)-ord('a')] = freq[ord(ch)-ord('a')] + 1
  for ch in B:
    freq[ord(ch)-ord('a')] = freq[ord(ch)-ord('a')] - 1

  for c in freq:
    if c!=0:
      return 0
  return 1       




def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    A  = input("String_1: ")
    B  = input("String_2: ")
    x = anagrams(A,B)
    print(f":::{A} And {B} are Anagrams \n if returns 1 , if returns 0 then are not Anagrams:::\n Returning ::=> {x}")
    n = n-1


if __name__ == "__main__":
  main()