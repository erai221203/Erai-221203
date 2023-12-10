e=int(input('Enter your ENGLISH mark:'))
m=int(input('Enter your MATHS mark:'))
p=int(input('Enter your PHYSICS mark:'))
c=int(input('Enter your CHEMISTRY mark:'))
cs=int(input('Enter your COMPUTER mark:'))

total=(e+m+p+c+cs)
avg=total/5

print('Total=',total)
print('Average=',avg)

if avg>=90 and avg<100:
    print('ENGINEER')
elif avg>=80 and avg<90:
    print('DOCTOR')
elif avg>=70 and avg<80:
    print('ARCHIETECT')
elif avg>=60 and avg<70:
    print('OTHERS')
else:
    print('')

