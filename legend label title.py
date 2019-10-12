import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

x1 = [5,9,3]
y1 = [1,9,6]

plt.plot(x,y , color = 'blue' , label = 'line 1')
plt.plot(x1,y1 , color = 'green' , label = 'line 2')

plt.xlabel("x axis")
plt.ylabel("y axis")

plt.legend()
plt.show()