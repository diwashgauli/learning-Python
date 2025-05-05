#simple for loop
for i in range(10):
    print(i)

for i in range(1,11):
    print(i)

#simple multiplications
num=2
for i in range(1,11):
    print(f"2 * {i} : {2*i}")

num1=2
num2=8
for i in range(num1,num2+1):
    for j in range(1,11):
        print(f"{i} x {j}: {i*j}")
    print("\n")


#while loop

num=5

while num>0:
    print(num)
    num=num-1

#factorial
num =5
fact=1

while num>0:
    fact=fact*num
    num=num-1
print(fact)

#sum of digits of a number

num=123
sum=0
while num>0:
    tosum=num%10
    sum=sum+tosum
    num=num//10
print(sum)



#break and continue

for i in range(5):
    print(i)
    if i==3:
        break  #terminates the loop

for i in range(5):
    if i==3:
        continue  #it skips that particular iteration and continue
    print(i)

for i in range(10):
    pass  #to hold for later changes


#can use else in for loop 

for i in range(5):
    print(i)
    print("loop completed")


for i in range(5):
    print(i)
    if i==3:
        break
else:

    print("loop completed")



username="John.doe"

for i in range(len(username)):
    print(username[i])


for char in username:
    print(char)

    
  




