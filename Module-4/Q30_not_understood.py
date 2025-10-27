def subArrayOR(A):
  mod  = 10**9 + 7
  n  = len(A)
  last  = [-1]*31  # last occurrence of each bit
  res  = 0 

  for i in range(n):
    for bit in range(31):
      if(A[i]>>bit)&1:
        last[bit] = i 
      count = last[bit]+1    


def main():
  n  = int(input("How Many Inputs: "))
  while n>0:
    A  = list(map(int,input("A: ").split()))
    B  = subArrayOR(A)
    print(f"OutPut:=> {B}")
    n  = n-1

if __name__ == "__main__":
  main()