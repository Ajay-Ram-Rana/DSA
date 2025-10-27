def  unique_two(A):
  xor_all = 0
  for num in A:
    xor_all = xor_all ^ num

  rightmost_set_bit = xor_all & (-xor_all)
  x,y = 0,0
  for num in A:
    if num & rightmost_set_bit:
      x  = x ^ num
    else:
      y = y ^ num
  return sorted([x,y])         




def main():
  n  = int(input("HOw many Inputs : "))
  while n>0:
    A = list(map(int,input("A: => ").split()))
    p,q  = unique_two(A)
    print(f"Two Unique Numbers that appears only 1 times : => {p},{q}")
    n  = n-1


if __name__ == "__main__":
  main()