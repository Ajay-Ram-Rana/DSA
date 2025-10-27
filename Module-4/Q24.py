def Number_bit_one(A):
  count = 0
  while A>0:
    if A & 1:
      count = count + 1
    A = A>>1
  return count    


def main():
  n  = int(input("How many inputs : "))
  while n>0:
    A  = int(input("N: => "))
    m  = Number_bit_one(A)
    print(f"Number of 1's in {A} : => {m}")
    n  = n-1


if __name__ == "__main__":
  main()