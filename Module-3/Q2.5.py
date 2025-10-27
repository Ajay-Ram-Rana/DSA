def minor_diagonal_sum(matrix):
  row = len(matrix)
  sum = 0
  for i in range(row):
    sum = sum + matrix[i][row-1-i]
  return sum  


def main():
  n = int(input("How many inputs: "))
  while n>0:
    size = int(input("Size of the Square matrix: "))
    matrix = []
    for i in range(size):
      rows = list(map(int,input().split()))
      matrix.append(rows)
    x = minor_diagonal_sum(matrix)
    print(f"Minor diagonal sum : {x}")   
    n =n-1


if __name__ =="__main__":
  main()