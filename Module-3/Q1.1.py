def kth_smallest(A,B):
  A.sort()
  n  = len(A)
  return A[B-1]    






def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A = list(map(int,input("A: ").split()))
    B = int(input("B: "))
    m = kth_smallest(A,B) 
    print(f"{B}th smallest element in sorted {A}: => {m}")
    n=n-1


if __name__ == "__main__":
  main()