age=int(input("Enter your age: "))

if age>=18:
    print("Can vote")
elif age <=0:
    print("Invalid Input")
else:
    print("cannot vote")


#alternative
print("can vote") if age>=18 else print("cannot vote")
