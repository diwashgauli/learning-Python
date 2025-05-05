#to check palindrome
str=input("Enter any string to check wether it is palindrome or not: ")
reverse=str[::-1]
if str == reverse:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome.")
