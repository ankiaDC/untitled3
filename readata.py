# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open(r'C:\Users\ankia\Desktop\ankc.xlsx','r',encoding='gbk')as csvfile:
    plots = csv.reader(csvfile)
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y,lebal='i find in a minute')
plt.xlabel('x')
plt.ylabel('y')
plt.titie('duqu\ntubiao')
plt.legend()
plt.show()