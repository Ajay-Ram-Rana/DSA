def largest_palindrome(A):
  n = len(A)
  if n==0:
    return ""
  start , max_len = 0 , 1
  for i in range(n):
    l,r = i, i 
    while l>=0 and r<n and A[l]==A[r]:
      if r-l+1> max_len:
        start,max_len = l,r-l+1
      l = l-1
      r = r+1

    l,r = i,i+1
    while l>=0 and r<n and A[l]==A[r]:
      if r-l+1>max_len:
        start , max_len = l, r-l+1
      l = l-1
      r = r+1

  return A[start:start+max_len]     


def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A =  input("String: ")
    B = largest_palindrome(A)
    print(f"Largest Palindrome is  : => {B}")
    n =n-1 

if __name__ =="__main__":
  main()