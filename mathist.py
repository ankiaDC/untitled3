# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

population_ages = [22,25,34,73,25,41,27,29,43,9,18,35,45,51,38,76,84,81,67,90,93,54,88,94,93]

bins = [0,10,20,30,40,50,60,70,80,90]

plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('c\nt')


plt.show()
