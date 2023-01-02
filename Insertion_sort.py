def ins_sort(marks):
    # Traverse through 1 to len(a)
    for i in range(1, len(marks)):

        key = marks[i]

        # Move elements of a[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < marks[j]:
            marks[j + 1] = marks[j]
            j -= 1
        marks[j + 1] = key
    return marks

def top_five_marks(marks):
    print("Top five score are : ")
    cnt = len(marks)

    if cnt < 5:
        start, stop = cnt - 1, -1  # stop set to -1 as we want to print the 0th element
    else:
        start, stop = cnt - 1, cnt - 6

    for i in range(start, stop, -1):
        print(" {0:.2f}".format(marks[i]), end="\n")

marks=[]
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"students (Press ENTER after every students marks): ")
for i in range(0, n):
    ele = int(input())
    marks.append(ele)  # adding the element

print("The marks of",n,"students are : ")
print(marks)

flag=1;

ins_sort(marks)
top_five_marks(marks)
