def addOneToNumber(A):
  
  while len(A)>1 and A[0]==0:
    A.pop(0)
  n  = len(A)
  carry = 1
  for i in range(n-1,-1,-1):
    s = A[i]+carry
    A[i] = s%10
    carry = s//10
    if carry==0:
      break
  if carry:
    A.insert(0,carry)

  return A    



def main():
  n  = int(input("How many Inputs:"))
  while n>0:
    A  = list(map(int,input("A: => ").split()))
    B  = addOneToNumber(A)
    print(f"After Adding 1 :=> {B}")
    n  = n-1


if __name__ =="__main__":
  main()