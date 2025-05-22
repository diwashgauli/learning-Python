# lambda arguments:expression

square = lambda x: x**2
print(square(5))

add=lambda a,b: a+b
print(f"Addition: {add(3,4)}")


multiply=lambda a,b: a*b
print(f"Multiplication: {multiply(2,3)}")

increment= lambda x: x+1
print(f"Increment: {increment(10)}")

sub=lambda a,b: a-b
print(f"Sub: {sub(10,5)}")

mod= lambda a,b: a%b
print(f"Modular division is: {mod(10,5)}")

div=lambda a,b:a/b
print(f"Division: {div(10,5)}")



#map() function

fruits=["###apple###","###mango###","###organge###","###banana###"]

output= list(map(lambda a: a[3:-3],fruits))
sorted_output=sorted(output)
final =list(map(lambda a: a.upper(),sorted_output))
print(final)


#alternative
output=list(map(lambda x: x.strip("#").upper(),fruits))
sorted_output=sorted(output)
print(sorted_output)



#using normal function
def upper_case(x):
    return x.strip("#").upper()

output=list(map(upper_case,fruits))
sorted_output=sorted(output)
print(sorted_output)


#filter() methods

numbers=[1,2,3,4,5,6,7,8,9,10]
#using lambda function
even_numbers=list(filter(lambda x: x%2==0,numbers))
print(f"Using lambda Function: {even_numbers}")


def evenn_numbers(x):
    if x%2==0:
        return True
    else:
        return False

#using normal function.
even= list(filter(evenn_numbers,numbers))
print(f"Using Normal Function: {even}")


fruits = ['banana', 'apple', 'avocado', 'grape', 'papaya']

new_fruits = list(filter(lambda x: x.count('a') > 2, fruits))
print(new_fruits)



