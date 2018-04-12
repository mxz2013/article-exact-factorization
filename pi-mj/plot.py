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
#ggg=np.linspace(0.1,1.0,20)
w_0=1.0
tt = np.linspace(0.0, 5.0, 40)
gg = np.linspace(0.1,2.0,20 )
xx  = np.array(gg)
yy = np.array(tt)
xx_md, yy_md = np.meshgrid(xx,yy)

Occb=np.zeros((len(tt),len(gg)))
#print "v1_md", V1_mt
Occa=np.zeros((len(tt),len(gg)))

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
        n = 0
        Nel1 = 0
        Nel2 = 0
        while n <= 50:
            Nel1+=e_vecs[2*n,0]**2
            Nel2+=e_vecs[2*n+1,0]**2
            n+=1

        Occb[nt,ng] =e_vecs[0,0] /np.sqrt(Nel1)  ## pi(m=0, j=1)        
        Occa[nt,ng] = e_vecs[0,0] /np.sqrt(Nel2) ## pi(m=1,j=2)         

font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 14,}
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
fig = plt.figure()
#plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.05,hspace=None)
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122,projection='3d')

ax1.set_title('(a) $\pi_{mj}(m=0,j=1)$ ' ,fontdict=font)
ax2.set_title('(b) $\pi_{mj}(m=1,j=2)$' ,fontdict=font)
#ax3.set_title('(b) $v_2$' ,fontdict=font)

ax1.set_xlabel('$g$ (eV)',fontdict=font)
ax1.set_ylabel('$t$ (eV)',fontdict=font)
ax2.set_xlabel('$g$ (eV)',fontdict=font)
ax2.set_ylabel('$t$ (eV)',fontdict=font)
ax1.set_zlabel('$\pi$',fontdict=font)
ax2.set_zlabel('$\pi$',fontdict=font)

ax1.plot_wireframe(xx_md, yy_md, Occb)
#ax1.zaxis.set_major_locator(LinearLocator(8))
#ax1.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))
ax2.plot_wireframe(xx_md, yy_md, Occa)
#ax2.zaxis.set_major_locator(LinearLocator(8))
#ax2.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))

#ax1.axis([0,1 ,0,1])
#ax2.axis([0,1 ,0,1])


#ax3.scatter(xx_md, yy_md, V3_md)
#ax3.zaxis.set_major_locator(LinearLocator(10))
plt.tight_layout()
plt.savefig('pi-mj.pdf', format='pdf')
plt.savefig('pi-mj.eps', format='eps')
#
#p = PdfPages('color-band-t'+str("%02d"%(nt+1))+'.eps' )
#pp.savefig()
#pp.close()
print "Done nt"
plt.show()
