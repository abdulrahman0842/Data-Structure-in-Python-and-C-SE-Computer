cricket=[45,65,85,25,33,48]
badminton=[45,88,25,66,20,14]
football=[]

# no_stu_cri=int(input("Enter No. of Student Play Cricket: "))
# for i in range(no_stu_cri):
#     ck=int(input("Enter Students ID (Cricket): "))
#     c.append(ck)


# no_stu_bad=int(input("Enter No. of Student Play BadMinton: "))
# for i in range(no_stu_bad):
#     bm=int(input("Enter Students ID (BadMinton): "))
#     b.append(bm)


# no_stu_foot=int(input("Enter No. of Student Play Foot Ball: "))
# for i in range(no_stu_foot):
#     fb=int(input("Enter Students ID (Foot Ball): "))
#     f.append(fb)


#For Intersection
def intersection(list1,list2):
    inter=[]
    for i in list1:
        for j in list2:
            if i is j:
                inter.append(i)
    return inter


#For Union
def union(list1,list2):
    union=list1.copy()
    for i in list2:
        if i not in list1:
            union.append(i)
    return union

#For Difference
def difference(intersection_list,union_list):
    diff=[]
    for i in union_list:
        if i not in intersection_list:
            diff.append(i)
    return diff
    
    
inter=intersection(cricket,badminton)
uni=union(cricket,badminton)
difr=difference(inter,uni)

print("Players Who play both Cricket and Badminton: ",intersection(cricket,badminton))

print("Union of Player who play Cricket and Badminton: ",union(cricket,badminton))

print("Diiference of players who play either Cricket or Badminton but not both: ",difference(inter,uni))
