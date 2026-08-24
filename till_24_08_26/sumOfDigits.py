
def doSum(num):
    num = abs(num)
    sum = 0

    while num:
        sum += num % 10
        num //= 10

    return sum


def main():
    num = int(input("Enter a number: "))
    print(f"Sum of digits of {num} is {doSum(num)}")


if __name__ == "__main__":
    main()
