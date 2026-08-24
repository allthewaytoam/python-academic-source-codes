
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"

    res = 1
    for i in range(2, n + 1):
        res *= i

    return res


def main():
    num = int(input("Enter a number: "))
    print(factorial(num))


if __name__ == "__main__":
    main()
