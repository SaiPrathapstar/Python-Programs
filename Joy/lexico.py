def biggerIsGreater(w):
    ww = list(set(w))
    indx = -1
    l = [ord(ch)for ch in w]
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            indx = i
        else:
            continue
    if indx == -1:
        return "no answer"
    j = len(l) - 1
    for x in range(j,indx,-1):
        if l[x] > l[indx]:
            l[x], l[indx] = l[indx], l[x]
            break
    l[indx+1 : ] = l[len(l) - 1 : indx : -1]
    y = []
    for z in l:
        y.append(chr(z))
    ans = ''.join(y)
    return ans
print(biggerIsGreater("abcdefg"))