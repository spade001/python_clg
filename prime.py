num=7
for i in range(2,(7//2)+1):
    if num%i == 0:
        print(f"{num} is prime number")
        break
else:
    print(f"{num} is not prime")