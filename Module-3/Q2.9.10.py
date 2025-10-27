def longest_consecutive_ones(A):
    n = len(A)
    if n == 0:
        return 0

    # Array to store consecutive 1s ending at index i
    ones = [0] * n
    if A[0] == '1':
        ones[0] = 1

    for i in range(1, n):
        if A[i] == '1':
            ones[i] = ones[i - 1] + 1

    max_len = max(ones)
    total_ones = A.count('1')

    for i in range(1, n - 1):
        if A[i] == '0':
            left = ones[i - 1]
            right = 0
            j = i + 1
            while j < n and A[j] == '1':
                right += 1
                j += 1
            max_len = max(max_len, min(total_ones, left + 1 + right))

    return max_len
      



def main():
  n = int(input("How Many Inputs:"))
  while n>0:
    A = input("String of 1's and 0's : ")
    m = longest_consecutive_ones(A)
    print(f"Longest Consecutive Ones length: {m}")
    n = n-1


if __name__ == "__main__":
  main()