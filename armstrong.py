#2. check Armstrong number
num = int(input("Enter a number to check wether it is a armstrong number or not: "))
sum = 0
temp = num
n = len(str(num))  # number of digits

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")