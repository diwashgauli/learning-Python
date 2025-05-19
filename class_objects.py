class personn:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def greet(self):
            return f"Hello, my name is {self.name} and I am {self.age} years old."
        

#creating objects of class which automatically calls the constructor and initialize the values. 
#person1 is set as an argument on self and acts as person1.name,person2.age
person1=personn("BOB",24)
person2=personn("Alice",34)
person3=personn("Max",23)


print(person1.name)
print(person2.age)

message1=person1.greet()
message2=person2.greet()
message3=person3.greet()
print(message1)
print(message2)
print(message3)


class Person:
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age


    def greet(self,name,age):
            return f"Hello, my name is {name} and I am {age} years old."
    

p1=Person()

result=p1.greet("abc",20)
print(result)

