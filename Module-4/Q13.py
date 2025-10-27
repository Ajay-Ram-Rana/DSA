def spiral(N):
    A = [[0 for _ in range(N)] for _ in range(N)]

    top = 0
    bottom = N - 1
    left = 0
    right = N - 1
    num = 1

    while left <= right and top <= bottom:
        # Top row (left → right)
        for i in range(left, right + 1):
            A[top][i] = num
            num += 1
        top += 1

        # Right column (top → bottom)
        for i in range(top, bottom + 1):
            A[i][right] = num
            num += 1
        right -= 1

        # Bottom row (right → left)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                A[bottom][i] = num
                num += 1
            bottom -= 1

        # Left column (bottom → top)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                A[i][left] = num
                num += 1
            left += 1

    return A


def main():
    n = int(input("How many inputs: "))
    while n > 0:
        N = int(input("Give N :=> "))
        A = spiral(N)
        print(f"\nSpiral Matrix ({N}x{N}):")
        for row in A:
            print(*row)
        n -= 1


if __name__ == "__main__":
    main()
