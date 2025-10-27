def colorful_number(num):
  digits = [int(d) for d in str(num)]
  products = set()

  n  = len(digits)

  for start in range(n):
    prod = 1
    for end in range(start,n):
      prod = prod*digits[end]
      if prod in products:
        return 0
      products.add(prod)

  return 1
    


def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    num  = int(input("Number: "))
    x  = colorful_number(num)
    print(f"{num} colorful , if yes(1), if no(0): = > {x}")
    n  = n-1


if __name__ == "__main__":
  main()