# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

plt.figure(figsize=(100,50))
m = Basemap(llcrnrlon=77,llcrnrlat=14
            ,urcrnrlon=140,urcrnrlat=51,projection='lcc',
            lat_1=33,lat_2=45,lon_0=100)
m.drawcoastlines()
m.drawcountries(linewidth=1.5)
m.readshapefile(r'C:\Users\ankia\Downloads\CHN_adm_shp\CHN_adm1',
                'states',drawbounds=True)
ax = plt.gca()

for nshape,seg in enumerate(m.states):
    poly = Polygon(seg,facecolor='r')

    ax.add_patch(poly)

m.readshapefile(r'C:\Users\ankia\Downloads\TWN_adm_shp/TWN_adm0',
                'taiwan',drawbounds=True)
for nshape,seg in enumerate(m.taiwan):
    ploy = Polygon(seg,facecolor='r')

    ax.add_patch(poly)

plt.show()