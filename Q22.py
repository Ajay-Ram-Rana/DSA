def leaders(A):
  n = len(A)
  lead  = []
  maximum = float('-inf')
  for i in range(n-1,-1,-1):
    if A[i]>maximum:
      lead.append(A[i])
      maximum = A[i]

  lead.reverse()
  return lead
    

def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A = list(map(int,input("Array A: => ").split()))
    B  = leaders(A)
    print(f"Leaders:=> {B}")
    n  = n-1


if __name__ =="__main__":
  main()