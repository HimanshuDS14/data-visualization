from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


fig = plt.figure()
ax1 = fig.add_subplot(111,projection = '3d')

x = [1,2,3,4,5,6,7]
y = [6,4,3,2,9,6,1]
z = [3,1,6,4,7,9,3]

x2 = [-1,-2,-3,-4,-5,-6,-7]
y2 = [-6,-4,-3,-2,-9,-6,-1]
z2 = [3,1,6,4,7,9,3]


plt.scatter(x,y,z , color = 'cyan' , label = 'x,y,z')
plt.scatter(x2,y2,z2 , color = 'red' , label = 'x1,y1,z1')

ax1.set_xlabel("x axis")
ax1.set_ylabel("y axis")
ax1.set_zlabel("z axis")
plt.legend()

plt.show()