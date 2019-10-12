import matplotlib.pyplot as plt


x = [2,3,4,5,6,7]
y = [3,2,4,3,5,6]

plt.scatter(x,y , color = 'red' , marker="*")
plt.xlabel("x")
plt.ylabel("y")
plt.show()