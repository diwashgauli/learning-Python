#integer list
num = [1,2,3,4,5]

#indexing in list
print(num[0]) 
print(num[-1])

#slicing in list
print(num[1:4]) 
print(num[1:4:2])


#appending new elements in list 
num.append(6)
num.append(7)
#popping elements from list 
num.pop(0)
num.pop(3)

print(num)


#looping and conditionals,len()
num=[1,2,3,4,5]

for n in num:
    print(n)


#creating lists of lists 

matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


print(matrix) #outputs whole matrix
print(matrix[0]) #outputs [1,2,3]
print(matrix[0][0]) #outputs 1
print(matrix[-1][1]) #outputs 8



#sum of all elements of all elements in a matrix: assignment
matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
total=0
for i in range(0,3):
    for j in range(0,3):
        total+=matrix[i][j]
print(f"Sum of all elements of given matrix is: {total}")







