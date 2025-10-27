def scaler_mul(matrix,x):
  m  = len(matrix)
  n  =  len(matrix[0])
  for i in range(m):
    for j in range(n):
      matrix[i][j]  = matrix[i][j]*x
  return matrix    




def main():
  n  = int(input("How many inputs: "))
  while n>0:
    matrix = []
    size = int(input("Size of the Matrix:"))
    x  = int(input("Scaler: "))
    for i in range(size):
      rows = list(map(int,input().split()))
      matrix.append(rows)
    A  = scaler_mul(matrix,x)
    print(f"After Scaler multiplication by {x} the matrix :=> {A}")  
    n = n-1


if __name__ == "__main__":
  main()