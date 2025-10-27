def antidiagonal(size,matrix):
  A = []
  for i in range(size):
      A.append(matrix[i][size-1-i])
  return A    





def main():
  n  = int(input("How many inputs :"))
  while n>0:
    size = int(input("Size of square matrix: "))
    matrix = []
    for i in range(size):
      row = list(map(int,input().split()))
      matrix.append(row)
    x = antidiagonal(size, matrix) 
    print(f"Antidiagonal of the given Matrix : => {x}")
    n=n-1


if __name__ == "__main__":
  main()