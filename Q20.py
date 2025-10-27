#Q1. Best Time to Buy and Sell Stocks I
def maxProfit(A):
  if not A:
    return 0
  

  min_price = A[0]
  max_profit = 0
  for price in A[1:]:
      profit = price - min_price
      if profit>max_profit:
        max_profit = profit
      if price<min_price:
        min_price = price

  return max_profit        


def main():
  n = int(input("How many inputs: "))
  while n>0:
    A = list(map(int,input("Array A: ").split()))
    m  = maxProfit(A)
    print(f"Maximum profit => {m}")
    n=n-1



if __name__ =="__main__":
  main()