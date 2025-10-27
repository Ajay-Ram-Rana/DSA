def rotate_90deg(matrix):
  n  = len(matrix)
  if n==0:
    return ""
  for i in range(n):
    for j in range(i+1,n):
      matrix[i][j],matrix[j][i] = matrix[j][i] ,matrix[i][j]

  for k in range(n):
    matrix[k].reverse()

  return matrix      




def main():
  n  = int(input("how many inputs: "))
  while n>0:
    matrix  = []
    size = int(input("Size of the square Matrix : "))
    for i in range(size):
      rows  = list(map(int,input().split()))
      matrix.append(rows)
    X  = rotate_90deg(matrix)
    print(f"After Rotation 90 degree: {X}") 
    for i in X:
      print(" ".join(map(str, i))) 
    n = n-1


if __name__ == "__main__":
  main()