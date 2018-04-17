import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import csv
from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.axes_grid.inset_locator import inset_axes
import matplotlib.ticker as ticker


def nonblank_lines(f):
   for l in f:
      line = l.rstrip()
      if line:
         yield line
x_mb1=[] 
y_mb1=[]## real
y_ma1=[]## imag
lines_1 = [line.rstrip('\n') for line in
           open('../sig00_t2.00_g1.00.dat')]
for plotPair in nonblank_lines(lines_1):
    if not plotPair.startswith("#"):
        xANDy = plotPair.split()
        x_mb1.append(float(xANDy[0].rstrip('\r'))) 
        y_mb1.append(float(xANDy[1].rstrip('\r'))) 
        y_ma1.append(float(xANDy[2].rstrip('\r'))) 
x_mb2=[] 
y_mb2=[]
y_ma2=[]
lines_1 = [line.rstrip('\n') for line in
           open('../sig00_t2.00_g2.00.dat')]
for plotPair in nonblank_lines(lines_1):
    if not plotPair.startswith("#"):
        xANDy = plotPair.split()
        x_mb2.append(float(xANDy[0].rstrip('\r'))) 
        y_mb2.append(float(xANDy[1].rstrip('\r'))) 
        y_ma2.append(float(xANDy[2].rstrip('\r'))) 
x_mb3=[] 
y_mb3=[]
y_ma3=[]
lines_1 = [line.rstrip('\n') for line in
           open('../sig00_t2.00_g3.00.dat')]
for plotPair in nonblank_lines(lines_1):
    if not plotPair.startswith("#"):
        xANDy = plotPair.split()
        x_mb3.append(float(xANDy[0].rstrip('\r'))) 
        y_mb3.append(float(xANDy[1].rstrip('\r'))) 
        y_ma3.append(float(xANDy[2].rstrip('\r'))) 
x_mb4=[] 
y_mb4=[]
y_ma4=[]
lines_1 = [line.rstrip('\n') for line in
           open('../sig00_t2.00_g4.00.dat')]
for plotPair in nonblank_lines(lines_1):
    if not plotPair.startswith("#"):
        xANDy = plotPair.split()
        x_mb4.append(float(xANDy[0].rstrip('\r'))) 
        y_mb4.append(float(xANDy[1].rstrip('\r'))) 
        y_ma4.append(float(xANDy[2].rstrip('\r'))) 

x_mb5=[] 
y_mb5=[]
y_ma5=[]
lines_1 = [line.rstrip('\n') for line in
           open('../sig00_t2.00_g5.00.dat')]
for plotPair in nonblank_lines(lines_1):
    if not plotPair.startswith("#"):
        xANDy = plotPair.split()
        x_mb5.append(float(xANDy[0].rstrip('\r'))) 
        y_mb5.append(float(xANDy[1].rstrip('\r'))) 
        y_ma5.append(float(xANDy[2].rstrip('\r'))) 

font = {'family' : 'serif',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 15,}

plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                    wspace=0.00,hspace=0.00)
fig1=plt.subplot2grid((2,1),(1,0))
plt.ylabel('Im$\Sigma_{00}$ ', fontdict=font)
plt.plot(x_mb1,y_ma1, '-',color='k',linewidth=1.0, label="$g=1.0$")
plt.plot(x_mb1,y_ma2, '-',color='r',linewidth=1.0, label="$g=2.0$")
plt.plot(x_mb1,y_ma3, '.',color='b',linewidth=1.0, markevery=0.1, label="$g=3.0$")
plt.plot(x_mb1,y_ma4, '-.',color='g',linewidth=1.5, label="$g=4.0$")
plt.plot(x_mb1,y_ma5, '-',color='m',linewidth=1.0, label="$g=5.0$")
plt.legend(loc=2,prop={'size':13} )
plt.xlim((-4,6))
fig2=plt.subplot2grid((2,1),(0,0))
plt.title('$t=2.0$',fontdict=font)
plt.ylabel('Re$\Sigma_{00}$ ', fontdict=font)
plt.plot(x_mb1,y_mb1, '-',color='k',linewidth=1.0, label="$g=1.0$")
plt.plot(x_mb1,y_mb2, '-',color='r',linewidth=1.0, label="$g=2.0$")
plt.plot(x_mb1,y_mb3, '-o',color='b',linewidth=1.0, markevery=0.1, label="$g=3.0$")
plt.plot(x_mb1,y_mb4, '-.',color='g',linewidth=1.5, label="$g=4.0$")
plt.plot(x_mb1,y_mb5, '-',color='m',linewidth=1.0, label="$g=5.0$")
plt.xlim((-4,6))
fig2.get_xaxis().set_ticks([])
#fig1.xaxis.set_major_locator(ticker.MultipleLocator(1))
#fig2.xaxis.set_major_locator(ticker.MultipleLocator(1))
#plt.tight_layout()
plt.savefig('sig00-t2.0.eps', format='eps', dpi=1000)
plt.savefig('sig00-t2.0.pdf', format='pdf')
#
plt.show()

