num=1246
num1=num
sum=0
while(num!=0):
     tmp=num%10
     sum=sum*10+tmp
     num=num//10
print(sum)