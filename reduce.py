from functools import reduce

numbers=[1,2,3,4,5]

sum=reduce(lambda x,y:x+y,numbers)
print(f"Sum of numbers: {sum}")


numbers=[3,8,1,6,2]
max_num= reduce(lambda x,y:x if x>y else y,numbers)
print(f"Maximum number is: {max_num}")


words=["Hello"," ","World","!"]
sentence= reduce(lambda x,y:x+y,words)
print(f"Sentence is: {sentence}")


numbers=[1,2,3,4,5]
product=reduce(lambda x,y:x*y,numbers,1)
print(f"Product of all numbers is: {product}")


#os
import os
current_dir=os.getcwd()   #to get current directory that is learning python 
print(f"Current Directory is: {current_dir}")

files=os.listdir(current_dir)
print(f"Files are: {files}") #gives all the file names that is inside learning python directory 

# #create new directory 
# new_dir="new directory"
# os.mkdir(new_dir)

#random 
import random

random_number=random.randint(1,10)
print(random_number)

my_list=[1,2,3,4,5]
random.shuffle(my_list)
print(my_list)
#math
import math
sqrt=math.sqrt(25)

factorial_value=math.factorial(5)



