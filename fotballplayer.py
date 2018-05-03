# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.style.use('ggplot')

font = FontProperties(fname=r'c:\windows\fonts\simsun.ttc',size=12)

ability_size = 6
ability_lable = ['sp','de','ta','sc','bo','sh']


ax1 = plt.subplot(221, projection='polar')
ax2 = plt.subplot(222, projection='polar')
ax3 = plt.subplot(223, projection='polar')
ax4 = plt.subplot(224, projection='polar')

player = {
    'M':np.random.randint(size = ability_size, low=60,high=99),
    'H':np.random.randint(size=ability_size, low=60, high=99),
    'P':np.random.randint(size = ability_size, low=60,high=99),
    'Q':np.random.randint(size = ability_size, low=60,high=99)
}

theta = np.linspace(0,2*np.pi,6,endpoint = False)

theta = np.append(theta,theta[0])

player['M']=np.append(player['M'],player['M'][0])
ax1.plot(theta,player['M'],'r')
ax1.fill(theta,player['M'],'r',alpha=0.3)
ax1.set_xticks(([theta]))
ax1.set_xticklabels(ability_lable,y=0.1,fontproperties=font)
ax1.set_title(u'梅西',fontproperties=font,color='r',size=20)

player['H']=np.append(player['H'],player['H'][0])
player['P']=np.append(player['P'],player['P'][0])
player['Q']=np.append(player['Q'],player['Q'][0])

plt.show()