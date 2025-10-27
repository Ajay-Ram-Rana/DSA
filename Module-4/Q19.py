def unset_bit(A,B):
  return (A & ~(1<<B)) 

def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    A = int(input("A: (Any +ve Integer: )"))
    B = int(input("B: (Which index bit is to be set : )"))
    m = unset_bit(A,B) 
    print(f"After {B}th set or unset {A}  become : => {m}")
    n = n-1

if __name__ =="__main__":
  main()