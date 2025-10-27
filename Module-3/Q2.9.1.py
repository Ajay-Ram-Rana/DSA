def string_operation(A):
  B = A+A
  result = ""
  for i in B:
    if not i.isupper():
      result = result+i

  vowels = "aeiouAEIOU"
  for j in vowels:
    result = result.replace(j,"#")

  return result        



def main():
  n = int(input("How many inputs: "))
  while n>0:
    A = input("String:")
    B = string_operation(A)
    print(f"After String: {B}")
    n =n-1


if __name__ =="__main__":
  main()