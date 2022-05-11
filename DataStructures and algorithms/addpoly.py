 def addpoly(l1,l2):
    l3 = []
    l4 = []
    p1 = [x[1] for x in l1]
    p2 = [x[1] for x in l2]

    for i in range(max(len(l1) , len(l2))):
        for j in range(i,(min(len(l1) , len(l2)))):
            if l1[i][1] == l2[j][1]:
                l3.append( (l1[i][0]+l2[j][0] , l2[j][1]) )
                break
    p3 = [x[1] for x in l3]
    p1 = [x for x in l1 if x[1] not in p3]
    p2 = [x for x in l2 if x[1] not in p3]
    if p1 != []:
        l3.append(p1)
    if p2 != []:
        l3.append(p2)
    for i in range(len(l3)):
        if(l3[i][0] != 0):
            l4.append(l3[i])
    return(l4)