def even_count(A,B):
  prefix = [0]*len(A)
  final_arr = []
  count = 0
  for i in range(len(A)):
    if A[i]%2==0:
      count = count+1
    prefix[i] = count

  for l,u in B:
    if l==0:
      final_arr.append(prefix[u])
    else:
      final_arr.append(prefix[u]-prefix[l-1])
  return final_arr  
        



def main():
  n  = int(input("How Many Inputs: "))
  while n>0:
    A = list(map(int,input("Array=> ").split()))
    B_input =  input("Pairwise seperated by ;").split(';')
    B  = [list(map(int, pair.split()))  for pair in B_input]
    m = even_count(A,B)
    print(f"Number of even count in the give range: {B} = > {m}")
    n=n-1



if __name__ =="__main__":
  main()