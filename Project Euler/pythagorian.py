for a in range(1,1000):
    for b in range(1,1000):
        for c in range(1,1000):
            if((pow(a,2)+pow(b,2)==pow(c,2)) and (a+b+c==1000)):
                print(a*b*c)