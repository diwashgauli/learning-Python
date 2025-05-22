def greeting(name):
    print("Hello"+name)

def sum(a,b):
    result=a+b
    print("Result",result)
    return result

def diff (a,b):
    result =a-b
    print("Result",result)
    return result

def mul(a,b):
    result =a*b
    print("Result",result)
    return result

print("This will run anyway.")

if __name__ == "__main__":
    print("This line will run only if you run mymodule.py else it wont be triggered from toimport.py.")
    

