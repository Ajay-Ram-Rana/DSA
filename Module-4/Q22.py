def magic_number(A):
    power = 1
    ans = 0
    while A > 0:
        last_bit = A & 1        # check LSB
        ans += last_bit * (5 ** power)
        power += 1
        A = A >> 1              # right shift to process next bit
    return ans


def main():
    n = int(input("How many Inputs: "))
    while n > 0:
        A = int(input("A: any natural number: "))
        B = magic_number(A)
        print(f"{A}th magic number : {B}")
        n -= 1


if __name__ == "__main__":
    main()
