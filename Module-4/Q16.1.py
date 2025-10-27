def num_ones(A):
  count = 0
  while A:
    count = count+ (A & 1)
    A = A>>1
  return count  



def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    A  = int(input("Any +ve Integer: "))
    m  = num_ones(A)
    print(f"# of 1's in binary of {A}:: => {m}")
    n  = n-1


if __name__ == "__main__":
  main()