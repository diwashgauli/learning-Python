import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,3,5,7,11]

x1=[6,7,8,9,10]
y1=[2,3,5,7,11]

plt.plot(x,y, marker='o',linestyle='--',color='b',label='Prime Numbers')
plt.plot(x1,y1,marker='o',linestyle='-',color='r',label='Numbers')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Prime numbers plot')

plt.legend()
plt.show()
