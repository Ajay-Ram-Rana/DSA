def boundary_elements(A):
  n  = len(A)
  for i in range(n):
    print(A[0][i],end=" ")
    
  for j in range(1,n):
    print(A[j][n-1],end=" ")
    
  for k in range(n-2,-1,-1):
    print(A[n-1][k],end=" ")
    
  for l in range(n-2,0,-1):
    print(A[l][0],end=" ")
  print("\n")  




def main():
  n  = int(input("How Many Inputs:"))
  while n>0:
    rows_entry = input("Rows Entries with   ; => ").split(";")
    A = [list(map(int , i.strip().split())) for i in  rows_entry]
    print("A: => ")
    for i in A:
      print(*i)
    print("Boundary Elements : =>",end=" ")
    print("\n")  
    boundary_elements(A)
    
    
      
    n  = n-1

if __name__ =="__main__":
  main()