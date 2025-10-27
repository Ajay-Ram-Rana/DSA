def first_missing_Positive(A):
    n = len(A)
    
    # Step 1: Ignore useless numbers
    for i in range(n):
        if A[i] <= 0 or A[i] > n:
            A[i] = n + 1
    
    # Step 2: Mark presence
    for i in range(n):
        x = abs(A[i])
        if 1 <= x <= n:
            if A[x - 1] > 0:   # mark only once
                A[x - 1] = -A[x - 1]
    
    # Step 3: Find missing number
    for j in range(n):
        if A[j] > 0:
            return j + 1
    
    return n + 1


def main():
    t = int(input("How Many Test Cases: "))
    while t > 0:
        A = list(map(int, input("Array: ").split()))
        x = first_missing_Positive(A)
        print(f"First Missing Positive Number: {x}")
        t -= 1


if __name__ == "__main__":
    main()
