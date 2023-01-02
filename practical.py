def Bubble_Sort(percentage):
    n = len(percentage)
    for i in range(n):
        for j in range(n - i - 1):
            if percentage[j] > percentage[j + 1]:
                percentage[j], percentage[j + 1] = percentage[j + 1], percentage[j]

    print("Percentage of students after performing Bubble Sort on the list :")
    for i in range(len(percentage)):
        print(percentage[i])

        
def top_five_scores(a):
    cnt = 5
    top=a[-5:]
    top.reverse()
    print("Top Five Scores are: ")
    for i in top:
        print(i)
        
percentage=[]
n = int(input("Enter number of students whose Percentage are to be displayed : "))
print("Enter Percentage for",n,"students (Press ENTER after every students Percentage): ")
for i in range(n):
    ele = float(input())
    percentage.append(ele)

print("The Percentage of",n,"students are : ")
print(percentage)

Bubble_Sort(percentage)
top_five_scores(percentage)
