def addition(A,B):
  row  = len(A)
  col  = len(A[0])
  result = []
  for i in range(row):
    row_sum = [A[i][j]+B[i][j]  for j in range(len(A[i]))]
    result.append(row_sum)
  return result    



def main():
  n  = int(input("How many inputs: "))
  while n>0:
    first_matrix = []
    second_matrix = []
    size  = int(input("Size for Ist Matrix:"))
    for i in range(size):
      rows = list(map(int,input().split()))
      first_matrix.append(rows)

    size  = int(input("Size for IInd Matrix:"))
    for j in range(size):
      rows = list(map(int,input().split()))
      second_matrix.append(rows)
    x  = addition(first_matrix,second_matrix)
    print(f"After Add: => {x}")
    for k in x:
      print(" ".join(map(str,k)))     
    n  = n-1

if __name__ == "__main__":
  main()