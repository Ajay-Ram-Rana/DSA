def flip(A):
  n   =  len(A)
  arr = [1 if ch=='0' else -1 for ch in A]

  max_sum  = float('-inf')
  curr_sum  = 0
  start = 0
  ans = []
  for i in range(n):
    curr_sum = curr_sum+arr[i]
    if curr_sum>max_sum:
      max_sum = curr_sum
      ans = [start+1,i+1]

    if curr_sum<0:
      curr_sum = 0
      start = i+1

  return ans if max_sum>0 else []       


def main():
  n   = int(input("How many inputs:"))
  while n>0:
    A  = input("Binary String: ")
    B  = flip(A)
    print(f"String => {A} is after fliping : {B}")
    n = n-1


if __name__ == "__main__":
  main()