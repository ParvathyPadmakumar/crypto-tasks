M=935
M1=M//5
M2=M//11
M3=M//17
mi1=pow(M1,-1,5)
mi2=pow(M2,-1,11)
mi3=pow(M3,-1,17)
x=M1*mi1*2+M2*mi2*3+M3*mi3*5
x=x%M
print(x)