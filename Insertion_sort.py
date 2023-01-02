import array as arr

# Accept the Roll Numbers of the students

def accept_roll():
    a = arr.array('I', [])
    no_stud = int(input("Enter the number of Students : "))
    for i in range(0, no_stud):
        a.append(int(input("Enter the Roll Number : ")))
    return a


# Print the Roll Numbers of the Students

def print_roll(a):
    for i in range(0, len(a)):
        print("\t", a[i], end=" ")
    print()

# Linear Search

def linear_search(a, x):
    for i in range(len(a)):

        if a[i] == x:
            return i

    return -1





flag=1
while flag == 1:
        menu = "1. Accept Student Roll Numbers of students who attended training program\n" \
               "2. Display the Roll Numbers of students who attended training program\n" \
               "3. Linear Search \n" \
               "4. Exit \n "
        print(menu)
        choice = int(input("Enter your choice : "))

        if choice == 1:
            unsort_A = accept_roll()

        elif choice == 2:
            print_roll(unsort_A)

        elif choice == 3:
            roll = int(input("Enter the Roll Number to be search : "))

            index = linear_search(unsort_A, roll)
            if index != -1:
                print("Roll number", roll, " at the index", index, "has Attended the training program")
            else:
                print("Roll number", roll, "has not Attended the training program")
        elif choice==4:
            print("Thank You")
            flag=0
        else:
            print("Wrong choice")
            flag = 0

        
