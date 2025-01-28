p=28151
#g=primitive elements=generator
#primitive_element=pow(g,n,p)

for g in range(1,28150):
    H=set()
    for n in range(1,28150):
        H.add(pow(g,n-1,p))
    if(len(H)==28149):
        print(g)
        break