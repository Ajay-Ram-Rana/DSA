def unset_B_from_right(A,B):
  mask  = ~((1<<B)-1)
  return A & mask


def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A  = int(input("A: any +ve Integer : "))
    B  = int(input("B : number of bits from right to be 0(unset): "))
    C  = unset_B_from_right(A,B)
    print(f"{A}===>{C} \n After unset {B} bits from right :")
    n  = n-1


if __name__ == "__main__":
  main()