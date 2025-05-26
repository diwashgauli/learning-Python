def decorator1(x):
    def wrapper():
        print("Something Before function runs.")
        print("Start time")
        x()
        print("End time -start time")
    return wrapper
@decorator1
def say_hello():
        print("Hello!")

say_hello()



def decorator1(fun):
    def wrapper(*args, **kwargs):
        print("Before")
        fun(*args, **kwargs)
        print("After")
    return wrapper

@decorator1
def say_hello(x, y):
    print("hello", x, y)

say_hello("abc", "der")


#using great decorator

def great_decorator(greetings): 
    def decorator1(fun):
        def wrapper(*args, **kwargs):
                print("Before")
                fun(*args, **kwargs)
                print("After")
        return wrapper
    return decorator1

@great_decorator("hello")
def say_hello(a, b):
    print("hello", a, b)

say_hello("abc", "der")


import time

def execution_time(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        print(f"Execution time: {end_time-start_time:.4f}seconds")
        return result
    return wrapper

@execution_time
def example_funtion(n):
    total =0
    for i in range(n):
          total+=i
    return total


final_sum=example_funtion(5)
print("final sum is: ", final_sum) 
