import numpy as np
#from control import pzmap,TransferFunction
from scipy import signal as sig
from matplotlib import pyplot as plt

C = 1*(10**(-6))
R = 1*(10**3)

num = np.array([ -1.,    3/(R*C),   -1/(C*C*R*R)   ])
den = np.array([ 5,     15/(R*C),    5/(C*C*R*R) ])


H = sig.TransferFunction( num, den )
w, mag, phase = sig.bode(H)

phase_rad = phase * np.pi / 180

plt.figure()

plt.subplot(211)
plt.semilogx(w, mag)        # Bode magnitude plot
plt.grid()
plt.ylabel('Magnitud')


plt.subplot(212)
plt.semilogx(w, phase_rad)  # Bode phase plot
plt.grid()
plt.ylabel('Fase')

plt.show()

#pzmap(H, Plot=True, title='Pole Zero Map')


