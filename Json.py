import json #from where ?
user1={
    "username1":"username1",
    "password1":"password1"

}

print(type(user1)) #outputs type as dictionary 

user1= json.dumps(user1) #it changes the dictionary format into json
print(type(user1)) #output type as str because it is already converted into json string


user2={
    "username2":"username2",
    "password2":"password2"

}

with open('user.json','w') as file:
    json.dump(user2,file,indent=4)


with open('user.json') as file:
    user=json.load(file)  #when it loads it loads back to dictionary format.    #loads?

print(user)
print(type(user))

