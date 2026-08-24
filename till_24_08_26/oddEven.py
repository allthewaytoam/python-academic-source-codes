
def isEven(n):
    return not n & 1

def main():
    n = int(input("Enter a number: "))
    print(f"{n} is {"Even" if isEven(n) else "Odd"}")

if __name__ == "__main__":
    main()
