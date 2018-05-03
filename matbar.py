# -*- coding -*-
import matplotlib.pyplot as plt

plt.bar([1,3,5,7,9],[5,2,7,3,9],label = "example one")

plt.bar([2,4,6,8,10],[6,4,8,2,9],label="example two",color='#aaaaaa')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('epic graph\nanother live!cc')

plt.show()