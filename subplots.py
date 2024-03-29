import matplotlib.pyplot as plt
from matplotlib import style
import random


style.use('fivethirtyeight')
fig = plt.figure()


def create_plot():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)
    return (xs,ys)




ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)

x,y = create_plot()
ax1.plot(x,y)



x,y = create_plot()
ax2.plot(x,y)

x,y = create_plot()
ax3.plot(x,y)

plt.show()
