#This program is not working!!!
a = [1,2,3,4,5]
temp = 0
i = 0
for x in a :
    z = int(input(f"Enter {i+1} element : "))
    a[i] = z
    i+=1
for x in a :
    for y in a :
        if x > y :
            temp = x
            x = y
            y = temp
for x in a :
    print(x)