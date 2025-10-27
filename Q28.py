def min_swap(A,B):
  n  =  len(A)
  k  = sum(1 for x in A  if x<=B)
  if k==0 or k==1:
    return 0
  
  bad  =  sum(1 for x in A[:k] if x>B)
  m_swap = bad

  for i in range(k,n):
    if A[i-k]>B:
      bad  =  bad-1
    if A[i]>B:
      bad = bad+1
    m_swap =  min(bad, m_swap)
  return m_swap    

  





def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A = list(map(int,input("A: => ").split()))
    B = int(input("B: => "))
    m = min_swap(A,B)
    print(f"Minimum Swap for all elements less than {B}: => {m}")  
    n=n-1


if __name__ =="__main__":
  main()