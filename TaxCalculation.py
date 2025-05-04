status=input("Enter your marial status: [M/U]")
salary=int(input("Enter your salary: "))
status=status.upper()
if status=='M':
    if salary>=100000:
        print(f"Your Tax to be paid is: {salary*0.1}")
    else:
        print(f"Your Tax to be paid is: {salary*0.8}")
else:
    if salary>=100000:
        print(f"your tax to be paid is: {salary*0.12}")
    else:
        print(f"your tax to be paid is: {salary*0.18}")
