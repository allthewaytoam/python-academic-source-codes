def inp():
    name=[]
    marks=[]
    n=5
    for i in range(n):
        nm=input("Enter name of student: ")
        if nm in name:
            print("Duplicate entry found. Please enter unique name.")
        else:
            mrk=int(input("Enter marks of student: "))
            name.append(nm)
            marks.append(mrk)
    return name, marks


def maxMinDisp(name, marks):
    max_marks_index = marks.index(max(marks))
    min_marks_index = marks.index(min(marks))
    print(f"Student with highest marks: {name[max_marks_index]} with marks {marks[max_marks_index]}")
    print(f"Student with lowest marks: {name[min_marks_index]} with marks {marks[min_marks_index]}")


def main():
    name, marks = inp()
    maxMinDisp(name, marks)


if __name__=="__main__":
    main()