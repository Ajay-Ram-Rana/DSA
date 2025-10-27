def sub_array(A,B,C):
  arr = []
  for i in range(B,C+1):
    arr.append(A[i])
  return arr  





def main():
  n = int(input("How many Inputs: "))
  while n>0:
    A = list(map(int,input("Array A: ").split()))
    B = int(input("Ist integer:"))
    C = int(input("IInd Integer:")) 
    D = sub_array(A,B,C)
    print(f"SubArray => {D}")
    n=n-1



if __name__ =="__main__":
  main()