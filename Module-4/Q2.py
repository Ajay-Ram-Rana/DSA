def bagger_sum(result,m):
    final = [0]*m
    for L,R,P in result:
        final[L-1] = final[L-1] + P
        if R<m:
            final[R] = final[R] - P


    for i in range(1,m):
        final[i] = final[i] + final[i-1]         

        
    return final    



def main():
    n = int(input("How many Inputs: "))
    result = []

    while n > 0:
        m  = int(input("Integer: "))
        rows = input("Entries (rows separated by ; and numbers by space): ").split(";")
        for row in rows:
            entry = list(map(int, row.strip().split()))
            result.append(entry)
        n -= 1

    B  = bagger_sum(result,m)
    print(f"Array {result} => {B}")


if __name__ == "__main__":
    main()
