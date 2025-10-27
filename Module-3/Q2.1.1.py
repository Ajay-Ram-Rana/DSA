def antiDiagonals(size ,matrix):
  A = [[0]*size for _ in range(2*size-1)]
  
  for i in range(size):
    for j in range(size):
      A[i+j][i] = matrix[i][j]
  return A    

     
def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    size = int(input("Size of Square Matrix: "))
    matrix = []
    for i in range(size):
      row  = list(map(int,input().split()))
      matrix.append(row)
    x  = antiDiagonals(size , matrix)
    print(f"All Anti Diagonals of Given Matrix : => {x}")
    for j in x:
      print(" ".join(map(str, j)))
    n=n-1

if __name__ == "__main__":
  main()