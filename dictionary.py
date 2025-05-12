user={
    'email': 'bob@bob.com',
    'password' : 'bob123',
    (1,2) : 'location'
    }

print(user['email'])
print(user['password'])
print(user.get('email')) #alternate way
print(user[(1,2)]) #used in tictactoe to store some value in that particular position
user['email']='bobisbob@example.com'
print(user['email'])

# print(user['address']) gives error when it doesnt find address key in the dictionary
print(user.get('address')) #returns None when it doesnt find address key in the dictionary if default value has been set it returns that value.


#pop and delete

del user['password'] #remove the key-value pair that is mentioned
print(user.pop('email')) #remove the key-value pair that is mentioned and also returns the value of that key value pair
print(user)



user1={
    'email': 'bob@bob.com',
    'password' : 'bob123',
    (1,2) : 'location'
    }

print(user1.keys())
print(user1.values())
print(user1.items())

#looping
for key, value in user1.items():  #tuple unpacking
    print(f"{key}->{value}")

#dictionary comprehension
fruits=['apple','banana','grapes']

word_count = {word:len(word) for word in fruits}
print(word_count)

user2={
    'username':'bob.bob',
    'password':'password',
    'address':{
        'province':'Bagmati',
        'district':'Lalitpur',
        'state':'Lalitpur'

    }
}
print(user2['address']['province'])

#assignment
# task=[
#     { 'task':'goto market', 'is_completed':True,
#      'Task':'learn python','is_completed':False}
# ]