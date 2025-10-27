def reverse_inRange(A,B,C):
  while B<C:
    A[B] ,A[C] = A[C] , A[B]
    B = B+1
    C = C-1 
  return A    




def main():
  n = int(input("How manay inputs :"))
  while n>0:
    A = list(map(int,input("Array: ").split()))
    B = int(input("Starting index:"))
    C = int(input("Ending index:"))
    x = reverse_inRange(A,B,C)
    print(f"After Reverse according to Given index : {x}")
    n = n-1 



if __name__ =="__main__":
  main()