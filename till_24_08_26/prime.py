def isPrime(num):
    if num<=1:
        return False
    c = 0
    for i in range(2, num//2+1):
        if not num % i:
            c+=1

    return not c


def main():
    num = int(input("Enter a number: "))
    print(f"{num} is {'Prime' if isPrime(num) else 'Not Prime'}")


if __name__ == "__main__":
    main()