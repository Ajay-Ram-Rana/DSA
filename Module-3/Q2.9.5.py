def Alphanumeric(A):
    for ch in A:  # iterate over characters, not indexes
        if not ch.isalnum():
            return 0
    return 1


def main():
    n = int(input("How many inputs: "))
    while n > 0:
        A = list(input("Alphanumeric String: "))   # read the string
        m = Alphanumeric(A)
        print(f"Alphanumeric : {m}")
        n -= 1


if __name__ == "__main__":
    main()
