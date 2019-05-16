import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sig
from splane import bodePlot, pzmap

#%%  
# Definimos los parámetros de la transferencia:
alfa_max = 0.5
n        = 7

e   = (10**(alfa_max*0.1) - 1)**0.5
wnb = e**(-1/n)

w01 = 1 * wnb * 1000
Q1 = 0.555
K1 = 5 
num1 = np.array([ K1 * w01**2 ])
den1 = np.array([ 1., w01 / Q1, w01**2 ])

w02 = 1 * wnb * 1000
Q2 = 0.802
K2 = 2
num2 = np.array([ K2 * w02**2 ])
den2 = np.array([ 1., w02 / Q2, w02**2 ])

w03 = 1 * wnb * 1000
Q3 = 2.247
K3 = 1
num3 = np.array([ K3 * w03**2 ])
den3 = np.array([ 1., w03 / Q3, w03**2 ])

w04 = 1 * wnb * 1000
K4 = 1
num4 = np.array([ K4 * w04 ])
den4 = np.array([ 1., w04 ])

numer = np.polymul(num1,num2)
denom = np.polymul(den1,den2)

numer = np.polymul(numer,num3)
denom = np.polymul(denom,den3)

numer = np.polymul(numer,num4)
denom = np.polymul(denom,den4)


H = sig.TransferFunction( numer, denom )

_, axes_hdl = bodePlot(H)

plt.sca(axes_hdl[0])

plt.gca

pzmap(H)

plt.show()