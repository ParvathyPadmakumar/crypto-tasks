#If we subtract a smaller number from a larger one (we reduce a larger number), GCD doesn’t change. So if we keep subtracting repeatedly the larger of two, we end up with GCD.

def gcd(a,b):
    global big
    global small
    big=max(a,b)
    small=min(a,b)
    while(big!=small):
        big=big-small
        if(big<small):
            small,big=big,small
    return small
a,b=map(int,input().split())
def gcd2(a,b):
    
    while(b!=0):
       a,b=b,a%b
    return a




print(gcd(a,b))
print(gcd2(a,b))



