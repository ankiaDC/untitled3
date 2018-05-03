#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt

silces = [2,5,9,11]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(silces,labels=activities,colors=cols,startangle=90,
        shadow=True,explode=(0,0.1,0,0),autopct='%1.1f%%')

plt.title('bingtu\nshili')

plt.show()