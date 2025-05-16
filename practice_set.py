
# Define vowels
string1 = "Hello world abc aaaa e iou aeiou"
words = string1.split()

vowels = "aeiouAEIOU"
vowel_count = 0

for word in words:
    is_vowel_word = True  # reset for each word

    for char in word:
        if char not in vowels:
            is_vowel_word = False
            break

    if is_vowel_word:
        vowel_count += 1

print("Number of vowel words:", vowel_count)




#converting sting helloworld into Hello World.
string1 = "helloworld"

string2 = string1[:5] + " " + string1[5:]

string2 = string2.title()

print(f"helloworld -> {string2}")

#Taking input from user and adding in between the Hello and World
#converting normal string into list of strings 
string1 = "Hello World"

string2 = [word.lower() for word in string1.split()] #list comprehension 

print(f"'Hello World' ->{string2}")

#adding new word taken from user in between hello and python 
string1='hello python'
print(string1)
string2=input(f"Enter any word you wanna add with {string1}: ")

string3=string1.split()

print(f"{string3[0]} {string2} {string3[1]}")



list1=[1,2,3,4,5,6]

list2=[i for i in list1 if i%2!=0]
print(list2) 


#tuple unpacking
tup = ("apple","banana","grapes")
tup1,tup2,tup3=tup
print(tup1)
print(tup2)
print(tup3)



from collections import Counter

lst = [1,1,1,2,2,3,3,3,3,3,4,5,6,7,8]

count = Counter(lst)

result = [i for i in lst if count[i] <= 2]

print(result)



#single valued tuple
single_tuple=(2,)
print(type(single_tuple))


#empty list

list=[]
print(type(list))


#common in two sets
set1 = {1,2,3}
set2 = {2,3,4}
set3 = set1.intersection(set2)
print(f"common elements between two sets are: {set3}")


#calculating total marks and making new key value pair in a dictionary
student = {
    "name": "abc",
    "age": 20,
    "marks": [10, 20, 30, 40]
}

total_marks=0
for i in range (len(student['marks'])):
    total_marks+= student['marks'][i]

    student['total_marks_obtained']=total_marks

print(student)



#sum div multi ....

def addition():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Sum of two numbers is: {a + b}")

def subtraction():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Difference of two numbers is: {a - b}")

def multiplication():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Multiplication of two numbers is: {a * b}")

def division():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Division of two numbers is: {a / b}")

def exponential():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Exponentiation of two numbers is: {a ** b}")

def modulus():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b == 0:
        print("Error: Modulus by zero is not allowed.")
    else:
        print(f"Modulus of two numbers is: {a % b}")

def menu():
    print("Select operation:")
    print("1. Addition ")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division (/)")
    print("5. Exponentiation (**)")
    print("6. Modulus (%)")

    choice = input("Enter choice (1-6): ")

    if choice == '1':
        addition()
    elif choice == '2':
        subtraction()
    elif choice == '3':
        multiplication()
    elif choice == '4':
        division()
    elif choice == '5':
        exponential()
    elif choice == '6':
        modulus()
    else:
        print("Invalid input. Please select a number between 1 and 6.")

menu()


#factorial using recursive function
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return  n * fact(n - 1)
    
num=int(input("Enter number you wanna calculate factorial of: "))
print(f"factorial of {num} is : {fact(num)}")

#writing content on file
content = """
Hello! Hi to demofile.txt
This file is for tested purposes.
Bad Luck!
"""

with open('test.txt','w') as file:
    file.write(content)
    
print("content written sucessfully.")

#reading from file
with open('test.txt') as file:
    content=file.read()
#updating from file using .replace(old,new) method.
content=content = content.replace("Hi", "hey").replace("tested", "testing").replace("Bad", "Good")


with open('test.txt','w') as file:
    file.write(content)

print("content updated sucessfully in the file.")
