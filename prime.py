#Assignments
#1. check prime number.
num = int(input("Enter any number you want to check wether it is prime or not: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a Prime number")


#sum and product of all from 1 to 100

sum=0
product=1
for i in range(1,101):
    sum+=i
    product*=i

print(f"Sum and Product of all numbers from 1 to 100 are: {sum} and {product} respectively.")