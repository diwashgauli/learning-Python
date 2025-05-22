#import traceback  -> traceback.print_exc() point out the lines where error has occured 
# #builtinexceptionhandling
# def divison():
#     try:
#         x=int(input("enter the number first: "))
#         y=int(input("enter the number second: "))
#         result=x/y
#         print("result: ",result)

    # except ZeroDivisionError as e:
    #     print(e)
    #     # print("value entered for y is Zero: ")
    #     # y=int(input("enter the number second once again: "))
    #     # result=x/y
    #     # print("result: ",result)
    #     divison()


    # except ValueError as e:
    #     print(e)

    #     # print("Cannot accept characters, Please Enter number.")
    #     # if type(x)==str:
    #     #     x=int(input("enter the number first: "))
    #     # else:
    #     #     y=int(input("enter the number second: "))
    #     # result=x/y
    #     # print("result: ",result)
    #     divison()

#     except Exception as e:
#         print(e)
#         divison()
    
#     finally:
#         print("program execution sucess !")

# divison()

#custom exception (left to do! before commit)


try:
    x=int(input("enter your age: "))
    if x>100:
        raise Exception("sorry age cannot be above 100")
    elif x==0:
        raise Exception("Sorry Age cannot be zero.")
    print(f"your age is: {x}")

    
except Exception as e:
    print(e)
    x=int(input("Re-Enter your age: "))
    print(f"your age is: {x}")







