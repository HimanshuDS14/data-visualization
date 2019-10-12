import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.Figure()
ax1 = fig.add_subplot(111 , projection='3d')

x = [1,2,3,4,5]
y = [7,4,1,4,6]



plt.plot(x,y,z)


ax1.set_xlabel("x")
ax1.set_ylabel("y")


plt.show()