def sum_even_index(A,B):
  arr = []
  sum = 0
  final_arr = []
  for i in range(len(A)):
    if i%2==0:
      sum = sum+A[i]
    arr.append(sum)
    
  
  for L,R in B:
    if L==0:
      final_arr.append(arr[R])
    else:
      final_arr.append(arr[R]-arr[L-1])

  return final_arr
    


def main():
  n = int(input("How many inputs: "))
  while n>0:
    A  = list(map(int , input("Array A:=> ").split()))
    B_input  = input("Pairwise seperated by ;").split(';')
    B  = [list(map(int, pair.split())) for pair in B_input]
    C = sum_even_index(A,B)
    print(f"Final Output: => {C}") 
    n = n-1


if __name__ == "__main__":
  main()