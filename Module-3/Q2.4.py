def main_diagonal_sum(A):
  row = A[0]
  col = A[1]
  data = A[2:]
  matrix = []
  sum = 0
  for i in range(row):
    matrix.append(data[i*col:(i+1)*col])
  for j in range(row):
    sum = sum + matrix[j][j]

  return sum     



def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    A = list(map(int,input().split()))
    x =  main_diagonal_sum(A)
    print(f"Sum of Diagonal : {x}")
    n = n-1



if __name__ == "__main__":
  main()