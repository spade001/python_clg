num=153
num1=num
sum=0
while(num!=0):
     tmp=num%10
     sum+=tmp**3
     num=num//10
print(sum)
if num1 == sum:
    print("Number is Amstrong")
else:
    print("Not Amstrong")
