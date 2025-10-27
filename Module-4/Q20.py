def toggle_bit(A,B):
  return A ^ (1<<B)


def main():
  n  = int(input("How many inputs: "))
  while n>0:
    A  = int(input("A: => "))
    B  = int(input("B: => "))
    m  = toggle_bit(A,B)
    print(f"After toggle {B}th bit of {A} final Number :: => {m}")
    n  = n-1


if __name__ =="__main__":
  main()