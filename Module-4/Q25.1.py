def singleNumber(A):
  result = 0 
  for i in range(32):
    bit_sum = 0
    for num in A:
      if (num>>i)& 1:
        bit_sum = bit_sum + 1
    if bit_sum % 3 !=0:
      result = result | 1<<i 

  if result >=2**31:
    result = result - 2**32
  return result          



def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    A  = list(map(int,input("A:=> ").split()))
    m  = singleNumber(A)
    print(f"In {A} :=>  {m} is the number which is not repeated 3 times: ")
    n  = n-1



if __name__ == "__main__":
  main()