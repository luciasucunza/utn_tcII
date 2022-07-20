# filtros.py

"""
Created on Mon Jul 18 21:49:01 2022
@author: lucia
"""

#%%  Librerìas

import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sig
from splane import bodePlot, pzmap, grpDelay
from cmath import rect

#%%  Máxima Planicidad

# Plantilla
alfa_max = 1
alfa_min = 20
wp = 1000 
ws = 1725

# Cuentas
e = (10**(alfa_max/10)-1)**0.5
ws_n = ws/wp
n = np.log10((10**(alfa_min/10)-1)/(10**(alfa_max/10)-1)) / (2*np.log10(ws_n))
n = int(np.ceil(n))
# Ejercicios sin plantilla
n = 3
e = 1       # Butterworth, alfa_max = 3dB

z = np.zeros(0)
p = np.zeros(n, dtype=complex)
if n%2 == 0:
    for i in range(n):
        ang = np.pi*(n+1+i*2)/(2*n) 
        p[i] = rect(e**(-1/n), ang)
        print("p",i, " = ", np.round(p[i],3))
else:    
    for i in range(n):
        ang = np.pi*(i+(n+1)/2)/n 
        p[i] = rect(e**(-1/n), ang )
        print("p",i, " = ", np.round(p[i],3))

num, den = sig.zpk2tf(z,p,1)
H = sig.TransferFunction(den[n].real, den.real)
_, axes_hdl = bodePlot(H, label = 'MaxPlanicidad')

grpDelay(H, label = 'MaxPlanicidad')
plt.sca(axes_hdl[0])
plt.gca
pzmap(H, label = 'MaxPlanicidad')
plt.show()

#%%  Chebyshev
n = 3
ripple = 1
z = np.zeros(0)
p = np.zeros(n, dtype=complex)

e = (10**(ripple/10)-1)**0.5
a = np.arcsinh(1/e)/n

for i in range(n):
    ang = np.pi*(2*(i+1)-1)/(2*n)
    p[i] = complex(-np.sinh(a)*np.sin(ang), np.cosh(a)*np.cos(ang))
    print("p",i, " = ", np.round(p[i],3))

num, den = sig.zpk2tf(z,p,1)
H = sig.TransferFunction(den[n].real, den.real)
_, axes_hdl = bodePlot(H, label = 'Chebyshev')

grpDelay(H, label = 'Chebyshev')
plt.sca(axes_hdl[0])
plt.gca
pzmap(H, label = 'Chebyshev')
plt.show()


#%%  Bessel
num = np.array([ 1])
den = np.array([ 1., 6., 15., 15.])

H = sig.TransferFunction(den[n], den)
_, axes_hdl = bodePlot(H, label = 'Bessel')

grpDelay(H, label = 'Bessel')
plt.sca(axes_hdl[0])
plt.gca
pzmap(H, label = 'Bessel')
plt.show()