def strangeEquality(A):
  p = 1
  while p <=A:
    p = p<<1
  y = p
  x = (p-1)-A
  return x^y  



def main():
  n  = int(input("How many inputs:"))
  while n>0:
    A  = int(input("A: "))
    B  = strangeEquality(A)
    print(f"For {A} ,then answer => {B}")
    n  = n-1

if __name__ =="__main__":
  main()