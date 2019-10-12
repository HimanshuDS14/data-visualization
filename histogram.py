import matplotlib.pyplot as plt


population_ages = [22,55,62,45,21,22,34,42,42,85,99,102]

bins = [0,10,20,30,40,50,60,70,80,90]

plt.hist(population_ages , bins , histtype='bar' , color = 'cyan' , rwidth=0.8)
plt.xlabel("x")
plt.ylabel("y")
plt.show()