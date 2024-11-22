
x1=1
y1=1
def gcdExtended(a,b,x,y):
    if(a==0):
        return(b)
    gcd=gcdExtended(b%a,a,x1,y1)
    x=y1-(b//a)*x1
    y=x1
    return(gcd)
a,b=map(int,input().split())
x=1
y=1
g=gcdExtended(a,b,x,y)
print("g=",g)
