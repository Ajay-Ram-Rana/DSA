def good_pair(x,m):
  length  = len(x)
  count = 0
  for i in range(length):
    for j in range(1,length):
      if (i!=j) and (x[i]+x[j] == m):
        print(f"({x[i]},{x[j]}) => {m} ")
        count = count+1

  if count!=0:
    return 1
  else:
    return 0      
        

    

def main():
  n = int(input("How many inputs :"))
  while n>0:
    x = list(map(int,input("Array: ").split()))
    m  = int(input("+ve Integer:"))
    r  = good_pair(x,m)
    print(r)
    n = n-1




if __name__ == "__main__":
  main()