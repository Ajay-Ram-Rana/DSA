def sum_first_N_natural(A):
  if A<=1:
    return 1
  ans = sum_first_N_natural(A-1)+A
  return ans



def main():
  n  = int(input("How many inputs : "))
  while n>0:
    A  = int(input("Sum of first N natural number ::=> N=?===> "))
    B = sum_first_N_natural(A)
    print(f"Sum of first {A} numbers => {B}")
    n  = n-1


if __name__ == "__main__":
  main()