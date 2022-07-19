import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sig
from splane import bodePlot, pzmap

#%%  
# Definimos los parámetros de la transferencia:
alfa_max = 1
n        = 4

e   = (10**(alfa_max*0.1) - 1)**0.5
wnb = e**(-1/n)

w01 = 1 * wnb * 1000
Q1 = 0.541
K1 = 2 
num1 = np.array([ K1 * w01**2 ])
den1 = np.array([ 1., w01 / Q1, w01**2 ])

w02 = 1 * wnb * 1000
Q2 = 1.307
K2 = 5
num2 = np.array([ K2 * w02**2 ])
den2 = np.array([ 1., w02 / Q2, w02**2 ])

numer = np.polymul(num1,num2)
denom = np.polymul(den1,den2)


H = sig.TransferFunction( numer, denom )

_, axes_hdl = bodePlot(H)

plt.sca(axes_hdl[0])

plt.gca

pzmap(H)

plt.show()