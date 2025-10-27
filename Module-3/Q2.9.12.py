def transpose_matrix(matrix):
  n  = len(matrix)
  m  = len(matrix[0])
  transpose  = [[0]*n for _ in range(m)]
  for i in range(n):
    for j in range(m):
      transpose[j][i]  = matrix[i][j]
  return transpose    



def main():
  n  = int(input("How many Inputs : "))
 
  while n>0:
    size  = int(input("Size of Matrix:"))
    matrix  = []
    for i in range(size):
      rows = list(map(int,input().split()))
      matrix.append(rows)
    A = transpose_matrix(matrix) 
    print(f"Transpose: {A}")
    for j in A:
      print(" ".join(map(str,j)))
      
    n  = n-1


if __name__ =="__main__":
  main()