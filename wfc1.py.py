import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,2*np.pi,0.01)
y_sin=np.sin(x)
y_cos=np.cos(x)


plt.style.use('ggplot')
plt.plot(x,y_sin,color='r',linewidth=1,alpha=0.6,label="sin(x)")
plt.plot(x,y_cos,color='b',linewidth=1,alpha=0.6,label='cos(x)')
plt.legend(bbox_to_anchor=(0.2, 1), loc=1, borderaxespad=0.)
plt.show()