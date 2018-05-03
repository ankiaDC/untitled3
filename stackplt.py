# -*-coding:utf-8 -*-
import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,9,10]
eating = [2,4,7,5,3]
working = [7,6,9,6,4]
playing = [8,5,2,6,3]

plt.plot([],[],color='m',label='Sleeping',linewidth=5)
plt.plot([],[],color='c',label='Eating',linewidth=5)
plt.plot([],[],color='r',label='Working',linewidth=5)
plt.plot([],[],color='k',label='Playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','r','c','k'])

plt.xlabel('days\neach')
plt.ylabel('things\nalways')
plt.title('nowdays\ndoing')
plt.show()
