# Q5. Sum of Odd indexed elements in a range
def odd_index_sum(A,B):
  sum_odd = 0
  prefix = [0]*len(A)
  final_arr = []
  for i in range(len(A)):
    if i%2!=0:
      sum_odd = sum_odd+A[i]
    prefix[i] = sum_odd

  for l,u in B:
    if l==0:
      final_arr.append(prefix[u])
    else:
      final_arr.append(prefix[u]-prefix[l-1])
  return final_arr          


def main():
  n  = int(input("how many inputs:"))
  while n>0:
    A = list(map(int,input("array A:=> ").split()))
    B_input = input("pairwise seperated by ;").split(';')
    B  =  [list(map(int,pair.split()))  for pair in B_input]
    C  = odd_index_sum(A,B)
    print(f"Sum of all numbers at Odd index in given range: => {C}")

    n=n-1


if __name__ =="__main__":
  main()