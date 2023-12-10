n=int(input("Enter a number:"))
sum=0
while(n>0):
 a=n%10
 sum+=a
 n=n//10
print("The sum of digits is:",sum)
