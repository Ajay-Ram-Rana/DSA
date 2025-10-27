def insert_merge(A,B):
  result = []
  i = 0
  n  = len(A)
  while i<n and A[i][1]<B[0]:
    result.append(A[i])
    i=i+1
  while i<n and A[i][0]<=B[1]:
    B[0] = min(B[0],A[i][0])
    B[1] = max(B[1],A[i][1])
    i = i+1
  result.append(B)

  while i<n:
    result.append(A[i])
    i = i+1    
  return result    



def main():
  n = int(input("How Many Inputs:"))
  while n>0:
    entry = input("Entries seprated by ; ").split(";")
    A = [list(map(int,i.strip().split())) for i in entry]
    B  = list(map(int,input("Any Interval to be Merged:").split()))
    C  = insert_merge(A,B)
    print(f"After Insert & Merge : => {C}")
    n = n-1


if __name__ == "__main__":
  main()