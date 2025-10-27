def all_possible_subarray(A):
  sum  = 0
  n  = len(A)
  m  = len(A[0])

  for i in range(n):
    for j in range(m):
      sum  = sum + A[i][j]*(i+1)*(j+1)*(n-i)*(m-j)

  return sum     




def main():
  n  = int(input("How many Inputs:"))
  while n>0:
    entry = input("Entries: ").split(";")
    A = [list(map(int,i.strip().split())) for i in entry]
    x = all_possible_subarray(A)
    print(f"All Possible Subarray: =>{x}")
    n=n-1

if __name__ == "__main__":
  main()