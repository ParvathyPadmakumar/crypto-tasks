l=[2]
check=False
for i in range(2,10000000):
    for j in range(2,i):
        if(i%j!=0):
            check=True
        else:
            check=False
            break
    if(check):
        l.append(i)
    if(len(l)==10500):
        break
print(l[0:20])
print(l[10000])

