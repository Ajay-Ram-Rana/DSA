def special_index(A):
  n= len(A)
  totalEven = sum(A[i] for i in range(0,n,2))
  totalOdd = sum(A[i] for i in range(1,n,2))

  evenLeft = 0
  oddLeft = 0
  count = 0
  for i in range(n):
    if i%2 ==0:
      totalEven = totalEven-A[i]
    else:
      totalOdd = totalOdd-A[i] 

    newEvenSum = evenLeft + totalOdd
    newOddSum  = oddLeft + totalEven

    if newEvenSum == newOddSum:
      count= count+1

    if i%2==0:
      evenLeft=evenLeft+A[i]
    else:
      oddLeft = oddLeft+A[i] 

  return count              
        



def main():
  n  = int(input("How many Inputs:"))
  while n>0:
    A  = list(map(int,input("Array A: => ").split()))
    m  = special_index(A)
    print(m)
    n=n-1


if __name__ =="__main__":
  main()