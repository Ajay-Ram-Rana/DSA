def number_zeros(A):
  n  = len(A)
  m  = len(A[0])
  i,j = 0,m-1
  while i<n and j>=0:
    if A[i][j]==1:
      maxRow = i
      j = j-1
    else:
      i = i+1
  return maxRow      



def main():
  n  = int(input("How mny inputs: "))
  while n>0:
    rows_entry = input("Rows Elements: ").split(";")
    A = [list(map(int,i.strip().split())) for i in rows_entry]
    x = number_zeros(A)
    print(f"Maximum Number of 1,s in  Rows:=> {x}")
    n = n -1


if __name__ =="__main__":
  main()