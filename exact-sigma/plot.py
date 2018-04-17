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
g=np.linspace(0.0,5.0,6)
w_0=1.0
e=t=0.5
e_1=e-t
e_2=e+t
eta=0.1j
n=4
x = np.linspace(-5.0,5.0,500)
sig=np.zeros((n,n), dtype=np.complex)
for j in range(len(g)):
    gt=g[j]/np.sqrt(2.)
    sig00=[]
    sig01=[]
    sig02=[]
    for i in range(len(x)):
        w=x[i]
        for i in range (n):
            if i+1<n:
                sig[i][i]= gt*i/((i-1)*w_0+t-w-eta) + gt*(i+1)/((i+1)*w_0+t-w-eta)
            if i>=1 and i+1<n:
                sig[i-1][i+1]=(gt*np.sqrt(i)*np.sqrt(i+1))/((i+1)*w_0+t-w-eta)
                sig[i+1][i-1]=(gt*np.sqrt(i)*np.sqrt(i+1))/((i+1)*w_0+t-w-eta)
        sig00.append(sig[0,0])
        sig01.append(sig[0,1])
        sig02.append(sig[0,2])
    sig00=np.array(sig00)
    sig01=np.array(sig01)
    sig02=np.array(sig02)

    with open ('sig00'+'_t'+str("%.02f"%(t))+'_g'+str("%.02f"%(g[j]))+'.dat', 'w') as f:
        writer=csv.writer(f, delimiter='\t')
        writer.writerows( zip (x, sig00.real, sig00.imag))
    with open ('sig02'+'_t'+str("%.02f"%(t))+'_g'+str("%.02f"%(g[j]))+'.dat', 'w') as f:
        writer=csv.writer(f, delimiter='\t')
        writer.writerows( zip (x, sig02.real, sig02.imag))







    #e_val#s, e_vecs = LA.eig(H2)
    #idx =# e_vals.argsort()
    #e_val#s=e_vals[idx]
    #e_vec#s=e_vecs[:,idx]
    #n = 0#
    #Nel1 #= 0
    #Nel2 #= 0
    #while# n <= 50:
    #    N#el1+=e_vecs[2*n,0]**2
    #    N#el2+=e_vecs[2*n+1,0]**2
    #    n#+=1

    #Occb[#nt,ng] = Nel1          
    #Occa[#nt,ng] = Nel2          

#font = {'#family' : 'serif',
#        '#color'  : 'darkred',
#        '#weight' : 'normal',
#        '#size'   : 14,}
#from mpl_#toolkits.mplot3d import Axes3D
#from matp#lotlib.ticker import LinearLocator, FormatStrFormatter
#fig = plt#.figure()
##plt.subp#lots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.05,hspace=None)
#ax1 = fig#.add_subplot(121, projection='3d')
#ax2 = fig#.add_subplot(122,projection='3d')
#
#ax1.set_t#itle('(a) $n^{el}(j=1)$ ' ,fontdict=font)
#ax2.set_t#itle('(b) $n^{el}(j=2)$' ,fontdict=font)
##ax3.set_#title('(b) $v_2$' ,fontdict=font)
#
#ax1.set_x#label('$g$ (eV)',fontdict=font)
#ax1.set_y#label('$t$ (eV)',fontdict=font)
#ax2.set_x#label('$g$ (eV)',fontdict=font)
#ax2.set_y#label('$t$ (eV)',fontdict=font)
#ax1.set_z#label('$n$',fontdict=font)
#ax2.set_z#label('$n$',fontdict=font)
#
#ax1.plot_#wireframe(xx_md, yy_md, Occb)
##ax1.zaxi#s.set_major_locator(LinearLocator(8))
##ax1.zaxi#s.set_major_formatter(FormatStrFormatter('%.01f'))
#ax2.plot_#wireframe(xx_md, yy_md, Occa)
##ax2.zaxi#s.set_major_locator(LinearLocator(8))
##ax2.zaxi#s.set_major_formatter(FormatStrFormatter('%.01f'))
#
##ax1.axis([0,1 ,0,1])
##ax2.axis([0,1 ,0,1])
#
#
##ax3.scatter(xx_md, yy_md, V3_md)
##ax3.zaxis.set_major_locator(LinearLocator(10))
#plt.tight_layout()
#plt.savefig('Occ-electron.pdf', format='pdf')
#plt.savefig('Occ-electron.eps', format='eps')
##
##p = PdfPages('color-band-t'+str("%02d"%(nt+1))+'.eps' )
##pp.savefig()
##pp.close()
#print "Done nt"
#plt.show()
