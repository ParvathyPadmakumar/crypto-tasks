
num=1
check=False
while(check==False):
    for i in range(1,21):
        if(num%i==0):
            check=True
        else:
            check=False
            break
    if(check==True):
        print(num)
    num+=1