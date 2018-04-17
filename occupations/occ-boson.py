import numpy as np
import math
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import pylab
import csv
from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.axes_grid.inset_locator import inset_axes
import matplotlib.ticker as ticker
from PyAstronomy import pyasl
import matplotlib.cm as cm
from scipy.interpolate import interp2d
from scipy.interpolate import griddata, RectBivariateSpline
from numpy import linalg as LA

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
#ggg=np.linspace(0.1,1.0,20)
w_0=1.0
tt = np.linspace(0.0,5.0,30)
gg = np.linspace(0.0,5.0,30)
xx  = np.array(gg)
yy = np.array(tt)
xx_md1, yy_md1 = np.meshgrid(xx,yy)
xx_md2, yy_md2 = np.meshgrid(xx,yy)
#print "xmd",xx_md
#print "ymd", yy_md

Occm1=np.zeros((len(tt),len(gg)))
#print "v1_md", V1_mt
Occm2=np.zeros((len(tt),len(gg)))

Z_md=[]
for nt in range(len(tt)):
    E0_g2_list=[]
    E0_md_list=[]
    v0_g2_list=[]
    v0_md_list=[]
    t=tt[nt]
    e=t
    e_1=e-t
    e_2=e+t
    g_md=gg
    Z2=[]
    for ng in range(len(gg)):
        g=gg[ng]/np.sqrt(2.0)  # \tilde{g} of the paper
        n=200
        H2=np.zeros((n,n))
        for i in range (n):
            if 2*i<n:
                H2[2*i][2*i]=2*i*w_0-t
            if 2*i+1<n:
                H2[2*i+1][2*i+1]=(2*i+1)*w_0+t
            if i+1<n:
                H2[i][i+1]= H2[i+1][i]=np.sqrt(i+1)*g
        e_vals, e_vecs = LA.eig(H2)
        idx = e_vals.argsort()
        e_vals=e_vals[idx]
        e_vecs=e_vecs[:,idx]
        #n = 0
        Nel1 = e_vecs[0,0]**2 
        Nel2 = e_vecs[1,0]**2
        #while n <= 50:
        #    Nel1+=e_vecs[0,0]**2
        #    Nel2+=e_vecs[2*n+1,0]**2
        #    n+=1

        Occm1[nt,ng] = Nel1          
        Occm2[nt,ng] = Nel2          

font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 16,}
fig = plt.figure()
#plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.05,hspace=None)
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122,projection='3d')
ax1.set_title('(a) $n^{bos}(m=0)$ ' ,fontdict=font)
ax2.set_title('(b) $n^{bos}(m=1)$' ,fontdict=font)
#ax3.set_title('(b) $v_2$' ,fontdict=font)
ax1.set_xlabel('$g$ ',fontdict=font)
ax1.set_ylabel('$t$ ',fontdict=font)
ax2.set_xlabel('$g$ ',fontdict=font)
ax2.set_ylabel('$t$ ',fontdict=font)
ax1.set_zlabel('$n$',fontdict=font)
ax2.set_zlabel('$n$',fontdict=font)

ax1.plot_surface(xx_md1, yy_md1, Occm1, cmap=cm.coolwarm, linewidth=0.1,
                 antialiased=False)
#ax1.plot_wireframe(xx_md, yy_md, Occm1)
#ax1.zaxis.set_major_locator(LinearLocator(8))
#ax1.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))
#ax2.plot_wireframe(xx_md, yy_md, Occm2)
ax2.plot_surface(xx_md2, yy_md2, Occm2, cmap=cm.coolwarm, linewidth=0.1,
                 antialiased=False)
#ax2.zaxis.set_major_locator(LinearLocator(8))
#ax2.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))

#ax1.axis([0,1 ,0,1])
#ax2.axis([0,1 ,0,1])
# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

#ax3.scatter(xx_md, yy_md, V3_md)
#ax3.zaxis.set_major_locator(LinearLocator(10))
plt.tight_layout()

plt.savefig('Occ-boson.pdf', format='pdf')
plt.savefig('Occ-boson.eps', format='eps')
#
#p = PdfPages('color-band-t'+str("%02d"%(nt+1))+'.eps' )
#pp.savefig()
#pp.close()
print "Done nt"
plt.show()
