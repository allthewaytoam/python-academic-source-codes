
def noOfDig(num):
    if not num:
        return 1
    sum=0
    while num:
        sum+=1
        num//=10
    return sum


def calc(num, p):
    sum=0
    while num:
        sum+=((num%10)**p)
        num//=10
    return sum


def checkArmstrong(num):
    if calc(num, noOfDig(num)) == num:
        return True
    else:
        return False


def main():
    num = int(input("Enter a num: "))
    print(f"{num} is {'an Armstrong No.' if checkArmstrong(num) else 'Not an Armstrong No.'}")


if __name__ == "__main__":
    main()
