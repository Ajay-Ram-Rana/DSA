def search(A,B):
  row = len(A)
  col = len(A[0])
  i,j = 0, col-1
  ans = float('inf')
  while i<row and j>=0:
    if A[i][j]==B:
      pos = (i+1)*1009+(j+1)
      ans = min(ans,pos)
      j=j-1
    elif A[i][j]>B:
      j = j-1
    else:
      i = i+1
  return ans if ans!= float('inf') else -1         



def main():
  n = int(input("How many Inputs: "))
  while n>0:
    rows = input().split(";")
    A = [list(map(int,i.strip().split())) for i in rows]
    B = int(input("B:=> "))
    x = search(A,B)
    print(f"::=> {x}")

    n = n-1


if __name__ == "__main__":
  main()