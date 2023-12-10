num= int(input("enter the limit:")) 
n=num//3
m=num//5
t=0
for i in range(1,n+1):
    t=t+3*i
f=0
for i in range(1,m+1):
    if(f!=0):
        if(f%3==0 and f%5==0):
           f=f+5*i
print(t+f)
