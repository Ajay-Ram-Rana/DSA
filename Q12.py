def special(x):
  count = 0
  g_count = 0
  for ch in reversed(x):
    if ch =='G':
      g_count = g_count+1
    elif ch =='A':
      count =count+g_count
  return count      
    


def main():
  n = int(input("How many Inputs: "))
  while n>0:
    x = input("Give letters:").strip().upper()
    A = special(x)
    print(f"Total 'AG' are Present => {A}")
    n=n-1




if __name__ == "__main__":
  main()