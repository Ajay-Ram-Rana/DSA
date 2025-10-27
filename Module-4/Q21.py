def set_bit(A,B):
  return (1<<A)|(1<<B)


def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A = int(input("A: "))
    B = int(input("B: "))
    m = set_bit(A,B)
    print(f"After set {A}th bit and set {B}th bit ,\n Final Number :: {m}")
    n  = n-1

if __name__ == "__main__":
  main()