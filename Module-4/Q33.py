def timer(time):
  if time==0:
    print(time)
    return 
  print(time)
  timer(time-1)
  
   
  
  


def main():
  n  = int(input("How many inputs: "))
  while n>0:
    time = int(input("Time (min):: => "))
    timer(time)
    
    n  = n-1


if __name__ == "__main__":
  main()