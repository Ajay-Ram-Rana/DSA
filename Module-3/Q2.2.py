def column_sum(matrix):
  row = len(matrix)
  col = len(matrix[0])
  
  result = []
  for j in range(col):
    sum  = 0
    for i in range(row):
      sum = sum + matrix[i][j]
    result.append(sum)
  return result    



def main():
  n  = int(input("How many inputs: "))
  while n>0:
    matrix = []
    row  = int(input("Rows:"))
    col = int(input("Columns:"))
    for i in range(row):
      x = list(map(int,input().split()))
      matrix.append(x)
    sums = column_sum(matrix)
    print(f"Columns_Sum : {sums}")
    n = n-1


if __name__ =="__main__":
  main()