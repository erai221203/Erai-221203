def get_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
        
    return sum

num = int(input("Enter a number: "))
while num > 9:
    num = get_sum(num)
    print('the order is:') 
    print(num)
print("The sum of digits until a single digit is obtained is", num)
