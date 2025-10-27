def positive_factors(m):
  count = 0
  for i in range(1,m+1):
    if m%i==0:
      count = count+1
      print(i,end=" ")
      
  return count    



def main():
  n  = int(input("How many cases u want to try:"))
  while(n>0):
    m = int(input("Give Integer:"))
    f = positive_factors(m)
    print("\n Total  number of +ve factors : ",f)
    n=n-1


if __name__ == "__main__":
  main()