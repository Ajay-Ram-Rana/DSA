def non_repeated_trice(A):
  ans = A[0]
  n  = len(A)
  for i in range(1,n):
    ans = ans ^ A[i]
  return ans   


def main():
  n  = int(input("How many Inputs : "))
  while n>0:
    A  = list(map(int,input("A: => ").split()))
    m  = non_repeated_trice(A) 
    print(f"Given {A} :: => {m} is not repeated 3 times: ")
    n  = n-1

if __name__ == "__main__":
  main()