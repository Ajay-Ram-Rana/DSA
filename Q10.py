def total_array(A):
  sub_arr = []
  n = len(A)
  for i in range(n):
    for j in range(i,n):
      sub_arr.append(A[i:j+1])
  return sub_arr    

      
    





def main():
  n = int(input("How many Inputs :"))
  while n>0:
    A = list(map(int,input("Array A:=>").split()))
    B = total_array(A)
    print(f"Total SubArray=> {B}")
    n=n-1


if __name__ == "__main__":
  main()