def multpoly(l1,l2):
    def last(n):
        return n[-1]
    def sort(tuples):
        return sorted(tuples, key=last)
    if len(l1) < len(l2):
        (l1,l2) = (l2,l1)
    l3 = []
    for i in range(max(len(l1) , len(l2))):
        for j in range(i,(min(len(l1) , len(l2)))):
            l3.append( (l1[i][0]*l2[j][0] , l2[j][1]*2) )
    d = {x:0 for x, _ in l3}
    for name, num in l3: d[num] += name
    Output = list(map(tuple, d.items()))
    fin = sort(Output)
    return(fin)
multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])