# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

x= [1,2,3,4,5,6,7,8]
y = [5,7,3,9,2,7,4,9]
z =[4,6,7,8,3,1,9,5]
plt.scatter(x,y,label='st',color ='#aaaaaa',s =25,marker="o" )
plt.scatter(x,z,label='sc',color ='#000000',s =100,marker="o" )
plt.xlabel('x')
plt.ylabel('y')


plt.title('interesting/nGraph')
plt.legend()
plt.show()

