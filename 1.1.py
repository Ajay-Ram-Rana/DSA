import math


def positive_factor(x):
  count = 0
  sqrt_x = int(math.sqrt(x))
  for a in range(1,sqrt_x+1):
    if x%a==0:
      if (a == (x//a)):
        count=count+1
      else:
        count = count+2  
  return count


def main():
  n = int(input("How many cases u want to try:"))
  while n>0:
    x = int(input("Give +ve Integer:"))
    m = positive_factor(x)
    print("\n Total no of +ve factors  : ",m)
    n-=1



if __name__ =="__main__":
  main()