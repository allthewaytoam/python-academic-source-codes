import random
from collections import Counter


def displayMarks(Marks):
    print("Marks List: ", end="")
    for mark in Marks:
        print(mark, end=" ")
    print()


def listCreation():
    random.seed()
    Marks = []
    for _ in range(20):
        mark = random.randint(0, 100)
        Marks.append(mark)
    displayMarks(Marks)
    return Marks


def avg(Marks):
    tot = sum(Marks)
    avg = tot / len(Marks)
    print("Average Marks: ", avg)
    return avg


def moreThanAvg(Marks, Avg):
    count = 0
    for mark in Marks:
        if mark > Avg:
            count += 1
    print("Number of students with marks more than average:", count)


def mode(Marks):
    counter = Counter(Marks)
    most_common = counter.most_common(1)

    if most_common:
        mark, freq = most_common[0]
        print("Mode of the list:", mark)
        print("Occurrence count:", freq)
        return mark, freq
    else:
        print("List is empty")
        return None, 0


def main():
    marks = listCreation()
    avg_mark = avg(marks)
    moreThanAvg(marks, avg_mark)
    mode(marks)



if __name__ == "__main__":
    main()
