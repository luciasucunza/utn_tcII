# respuestas.py

"""
Created on Mon Jul 18 21:52:10 2022
@author: lucia
"""

#%%  Librerìas

import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sig
from splane import bodePlot, pzmap


#%%  Num-Den (SOS)
k = 1
w0 = 1
q = 1
num = np.array([ k*w0**2 ])
den = np.array([ 1., q/w0, w0**2 ])

H = sig.TransferFunction(num, den)
_, axes_hdl = bodePlot(H)

plt.sca(axes_hdl[0])
plt.gca
pzmap(H)
plt.show()

#%%  Num-Den 
num = np.array([ 1., 0, 0.5, 0])
den = np.array([ 1., 2., 2., 1.])

H = sig.TransferFunction(num, den)
_, axes_hdl = bodePlot(H)

plt.sca(axes_hdl[0])
plt.gca
pzmap(H)
plt.show()