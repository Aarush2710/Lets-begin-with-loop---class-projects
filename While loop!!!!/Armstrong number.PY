num1=int(input("Enter a three dight number  "))
sum=0
i=num1
while i > 0:
    digit = i %  10  #3
    sum=sum+digit**3 #0+27
    i = i//10 #15
if sum == num1:
    print("Armstrong number")
else:
    print("not a Armstrong number")