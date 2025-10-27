def good_subarray(A,B):
  n = len(A)
  count = 0
  prefix = [0]*(n+1)
  for i in range(n):
    prefix[i+1] = prefix[i]+A[i]

  for i in range(n):
    for j in range(i,n):
      sub_sum = prefix[j+1] - prefix[i]
      length = j-i+1
      if length % 2 == 0 and sub_sum<B:
        count = count+1
      elif length %2 == 1 and sub_sum>B:
        count = count+1
  return count         
    


def main():
  n = int(input("How many inputs : "))
  while n>0:
    A = list(map(int,input("A: => ").split()))
    B = int(input("B:(Sum)"))
    m = good_subarray(A,B)
    print(f"Number of Good SubArrays: => {m}") 
    n = n-1



if __name__ == "__main__":
  main()