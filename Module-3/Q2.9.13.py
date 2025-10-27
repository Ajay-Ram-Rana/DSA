def repeatNumber(A):
  n  = len(A)
  candidate1 = candidate2 = None
  count1 = count2 = 0

  for num in A:
    if candidate1 == num:
      count1 = count1+1
    elif candidate2 == num:
      count2 = count2+1
    elif count1 == 0:
      candidate1 = num
      count1 = 1
    elif count2 == 0:
      candidate2 = num
      count2 = 1
    else:
      count1 = count1 - 1 
      count2 = count2 - 1

  count1 = count2 = 0 
  for num in A: 
    if num==candidate1:
      count1=count1+1
    elif num == candidate2:
      count2 =count2+1

  if count1>n//3:
    return candidate1
  if count2>n//3:
    return candidate2

  return -1
             
    
       


def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A = list(map(int,input("List: ").split()))
    m = repeatNumber(A)
    print(f"for {A} :  => {m}")
    n  = n-1


if __name__ == "__main__":
  main()