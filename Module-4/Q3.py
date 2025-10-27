def merge_sort_overlapping(A):
  if not A:
    return []
  merged = [A[0]]

  for current in A[1:]:
    last = merged[-1]
    if current[0]<=last[1]:
      last[1] =  max(last[1],current[1])
    else:
      merged.append(current)

  return merged      




def main():
  n  = int(input("How many Inputs: "))
  while n>0:
    A = []
    entry = input("Entry:").split(";")
    for i in entry:
      x = list(map(int,i.strip().split()))
      A.append(x)
    B  = merge_sort_overlapping(A)
    print(f"for {A} \n Merge Overlapping : => {B}")  
    n  = n-1



if __name__ == "__main__":
  main()