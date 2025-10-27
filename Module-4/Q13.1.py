def spiral(N):
  A = [[0 for _ in range(N)]  for _ in range(N)]
  top  = 0
  bottom = N-1
  left = 0
  right = N-1
  num = 1

  while left<=right and top<=bottom:
    for i in range(left,right+1):
      A[top][i] = num
      num = num+1
    top = top+1
    for j in range(top,bottom+1):
      A[j][right] = num
      num  = num+1
    right = right-1

    if top<=bottom:
      for i in range(right,left-1,-1):
        A[bottom][i] = num
        num = num+1
      bottom = bottom-1
    if left<=right:
      for i in range(bottom,top-1,-1):
        A[i][left] = num
        num  = num+1
      left = left+1

  return A      





def main():
  n  = int(input("How many Inputs:"))
  while n>0:
    N  = int(input("N  => "))
    A = spiral(N)
    print(f"Spiral=> ({N}x{N}) Matrix : ")
    for i in A:
      print(*i)
    n  = n-1


if __name__ == "__main__":
  main()