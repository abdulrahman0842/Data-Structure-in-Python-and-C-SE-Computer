c=[45,65,85,25,33,48]
b=[45,88,25,66,20,14]
f=[]

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


def cri_int_bad(cricket,badminton):
    inter=[]
    for i in cricket:
        for j in badminton:
            if i is j:
                inter.append(i)
    return inter

print("Players Who play both Cricket and Badminton: ",cri_int_bad(c,b))

def cri_uni_bad(cricket,badminton):
    union=cricket.copy()
    for i in badminton:
        if i not in cricket:
            union.append(i)
    return union

# print("Union",cri_uni_bad(c,b))

def diff(intersection,union):
    diff=[]
    for i in union:
        if i not in intersection:
            diff.append(i)
    return diff
unt=cri_int_bad(c,b)
uni=cri_uni_bad(c,b)
difference=diff(unt,uni)
print("Diiference",difference)





