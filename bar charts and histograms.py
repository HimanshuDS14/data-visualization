import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,9,11]
y2 = [7,8,2,4,2]


plt.bar(x,y,label = 'bar1' , color = 'red')
plt.bar(x2,y2 , label = 'bar2' , color = 'blue')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()