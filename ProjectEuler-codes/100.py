sum=0
for i in range(1,101):
    sumsq=(i*(i+1)*(2*i+1))/6
    sum=sum+i
sqsum=pow(sum,2)
print(sqsum-sumsq)
