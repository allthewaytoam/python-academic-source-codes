
def isLeap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def main():
    year = int(input("Enter year: "))
    print(f"{year} is {"a 'Leap Year'" if isLeap(year) else "Not a 'Leap Year'"}")

if __name__ == "__main__":
    main()
