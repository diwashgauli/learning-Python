num=int(input("Enter any number to check:"))
if num %5 == 0 and num%3== 0:
    print("FiZZBUZZ")
elif num%3==0:
    print("FIZZ")
elif num%5==0:
    print("BUZZ")
else:
    print(num)
    

