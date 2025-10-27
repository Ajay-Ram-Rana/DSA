def maxSubArray(A, B, C):
    max_sum = 0
    for i in range(A):
        current_sum = 0
        for j in range(i, A):
            current_sum += C[j]
            if current_sum > B:
                break  # because elements are positive, no need to continue
            max_sum = max(max_sum, current_sum)
    return max_sum

def main():
    n = int(input("How many inputs: "))
    while n > 0:
        A = int(input("Size of Array A: "))
        B = int(input("Maximum allowed sum B: "))
        C = list(map(int, input("Array C: ").split()))
        if len(C) != A:
            print("Size of C does not match A")
        else:
            result = maxSubArray(A, B, C)
            print(f"Maximum subarray sum not exceeding B => {result}")
        n -= 1

if __name__ == "__main__":
    main()
