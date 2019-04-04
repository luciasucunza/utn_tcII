import numpy as np
from scipy import signal as sig
from matplotlib import pyplot as plt

R   = 1000
R3  = 1000
C   = 10**(-6)

num_a = np.array([ 1.,  -1/(R3*C) ])
den_a = np.array([ 1.,   1/(R3*C) ])

num_b = np.array([ -1., 3/(R*C), -1/((C*R)**2) ])
den_b = np.array([ 5,   5/(R*C),  5/((C*R)**2) ])

H_a = sig.TransferFunction( num_a, den_a )
w_a, H_a_mag, H_a_phase = sig.bode(H_a)
H_a_phase_rad = H_a_phase * np.pi / 180

H_b = sig.TransferFunction( num_b, den_b )
w_b, H_b_mag, H_b_phase = sig.bode(H_b)
H_b_phase_rad = H_b_phase * np.pi / 180

plt.figure()

plt.subplot(211)
plt.semilogx(w_a, H_a_phase_rad) 
plt.title('Fase - Ejercicio 4.1')
plt.grid()


plt.subplot(212)
plt.semilogx(w_b, H_b_phase_rad)  
plt.title('Fase - Ejercicio 4.2')
plt.grid()

plt.show()

