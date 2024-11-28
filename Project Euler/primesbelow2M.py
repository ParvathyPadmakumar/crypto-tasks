
def fastGenerator(M):
    sum=0
    result=[2,3]
    a=5
    b=7
    count=3
    factor=[5]       #caching factor
    threshold=25   #instead of calculating square-root on each candidate,
    while a<M:       #...I change threshold every other time
        if a==threshold:
            factor.append(result[count])
            threshold=factor[-1]**2
            count+=1
        elif all(a%k for k in factor):
            result.append(a)
        if b>=M:
            break
        elif b==threshold:
            factor.append(result[count])
            threshold=factor[-1]**2
            count+=1
        elif all(b%k for k in factor):
            result.append(b)
        a+=6
        b+=6
    
    for i in result:
        sum+=i
    return sum
print(fastGenerator(10))
