def row_col_zero(matrix):
  row = len(matrix)
  col = len(matrix[0])
  zero_rows = set()
  zero_col = set()
  for i in range(row):
    for j in range(col):
      if matrix[i][j]==0:
        zero_rows.add(i)
        zero_col.add(j)

  for i in range(row):
    for j in range(col):
      if i in zero_rows or j in zero_col:
        matrix[i][j]=0

  return matrix            


def main():
  n  = int(input("How many inputs: "))
  while n>0:
    size = int(input("Size of the Matrix: "))
    matrix = []
    for i in range(size):
      rows = list(map(int,input().split()))
      matrix.append(rows)
    A = row_col_zero(matrix)
    print(f"Required Matrix : {A}")
    for x in A:
      print(" ".join(map(str, x))) 
    n = n-1

if __name__ == "__main__":
  main()