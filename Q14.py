def equilibrium_index(A):
  left_sum = 0
  total_sum = sum(A)
  indices = []
  for i,num in enumerate(A):
    total_sum = total_sum - num
    
    if left_sum == total_sum:
       indices.append(i)

    left_sum = left_sum+num


  return indices   
    
      









def main():
  n  = int(input("How may inputs:"))
  while n>0:
    A= list(map(int,input("Array A: =>").split()))
    m = equilibrium_index(A)
    print(f"Equilibrium Index=> {m}")
    n=n-1



if __name__ =="__main__":
  main()