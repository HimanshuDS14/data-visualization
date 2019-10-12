import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [3,2,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

slices = [13,2,2,7]

activities = ["sleeping" , "eating" , "working" , "playing"]
colors = ["cyan" , "yellow" , "blue" , "red"]

plt.pie(slices , labels= activities , colors = colors , startangle=90 , shadow=True , explode=(0.1,0.1,0.5,0.1) , autopct='%1.1f%%')
plt.title("pie charts")
plt.show()