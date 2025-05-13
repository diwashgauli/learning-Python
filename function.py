#addition
def add():
    a=int(input("Enter number to add: "))
    b=int(input("Enter another number to add: "))
    sum1=a+b
    return sum1

sum1 =add()
print(sum1)

def add(a,b):
    sum2=a+b
    return sum2

print(add(1,2))

#factorial 
def factorial(n):
    total=0
    while n>0:
        total=total+n
        n=n-1
    return total

print(factorial(5))



#using tuple
def get_status(numbers):
    min_value =min(numbers)
    max_value= max(numbers)
    sum_value= sum(numbers)
    return min_value,max_value,sum_value

result=get_status([1,2,3,4,5])
print(result) #returns tuple

min_val,max_val,summ_val = get_status([1,2,3,4,5]) #tuple unpacking

print(f"Minimum value is: {min_val}, Maximum value is: {max_val}, and Sum of all is: {summ_val}")



#using list
def get_status_list(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    sum_value = sum(numbers)
    return [min_value, max_value, sum_value]  # returning as a list

result = get_status_list([1, 2, 3, 4, 5])
print(result)  # [1, 5, 15]
max_val = result[1]
min_val=result[0]
sum_vall=result[2]
print(f"Minimum value is: {min_val}, Maximum value is: {max_val}, and Sum of all is: {sum_vall}")




#  using dictionary 
def get_status_dict(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    sum_value = sum(numbers)
    return {
        "min": min_value,
        "max": max_value,
        "sum": sum_value
    }  # returning as a dictionary

result = get_status_dict([1, 2, 3, 4, 5])
print(result)  # {'min': 1, 'max': 5, 'sum': 15}

print(f"Minimum value is: {result['min']}, Maximum value is: {result['max']}, and Sum of all is: {result['sum']}")


#calculate price
def calculate_price(unit_price,qty=1,dis=0.1): #parameters with default arguments
    price=unit_price*qty
    dis=price*dis
    total =price-dis
    return total

price=calculate_price(100,3,0.1)
print(price)

