import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [3,2,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([] , [] , color = 'cyan' , label = "sleeping" , linewidth = 5)
plt.plot([] , [] , color = 'green' , label = "eating", linewidth = 5)
plt.plot([] , [] , color = 'red' , label = "working", linewidth = 5)
plt.plot([] , [] , color = 'orange' , label = "playing", linewidth = 5)


plt.stackplot(days , sleeping , eating , working , playing , colors = ['cyan' , 'green' , 'red' , 'orange'])
plt.xlabel("days")
plt.ylabel("daily routine")
plt.legend()
plt.show()