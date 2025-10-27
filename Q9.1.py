def rangeSum(A, B):
    # Build prefix sum array P where P[i] = sum of A[0..i-1]
    n = len(A)
    P = [0] * (n+1)
    for i in range(n):
        P[i+1] = P[i] + A[i]

    # Compute sums using prefix array
    arr = []
    for L, R in B:
        if L > R:  # handle reversed ranges if needed
            L, R = R, L
        arr.append(P[R+1] - P[L])
    return arr


def main():
    n = int(input("How many Inputs : "))
    while n > 0:
        A = list(map(int, input("Array A:=> ").split()))
        # Example input for B: "0 3;1 2"
        B_input = input("Array B (pairs separated by ';'):=> ").split(';')
        B = [list(map(int, pair.split())) for pair in B_input if pair.strip()]
        C = rangeSum(A, B)
        print(f"Output Array: => {C}")
        n -= 1


if __name__ == "__main__":
    main()
