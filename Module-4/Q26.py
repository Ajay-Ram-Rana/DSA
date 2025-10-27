def number_of_days(A):
  count = 0
  while A>0:
    if A & 1:
      count = count +1
    A = A>>1
  return count     


def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    A = int(input("A: => "))
    B = number_of_days(A)
    print(f"{A} Food Boomer Eats in {B} days: ")
    n  = n-1


if __name__ == "__main__":
  main()