def no_ones(A):
  dividend = A
  divisor = 2
  count = 0
  while dividend >= divisor:
    remainder  = dividend%2
    dividend = dividend//divisor
    if remainder==1:
      count = count+1

  return count+1    


def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A = int(input("Any +ve Integer: "))
    m = no_ones(A)
    print(f"# of 1's in {A} Binary Representation:=> {m}")
    n  = n-1


if __name__ == "__main__":
  main()