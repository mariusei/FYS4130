# Exercise 6c

import matplotlib.pylab as plt
from numpy import *


# plot pressure p as function of V for V in [0.4, 20]
# for T = 1.15, 1.0, and 0.85

def pressure(T, V):
    return 8.0 * T / float(3.0 * V - 1) - 3.0/float(V)**2

def pressure2(T, rho):
    return 8.0 * rho * T / (3.0 - rho) - 3.0 * rho**2

pressure = vectorize(pressure)
pressure2= vectorize(pressure2)

V   = linspace(0.4, 2.0, 500)
rho = linspace(0.0, 2.0, 500)
P1  = pressure(1.15, V)
P2  = pressure(1.0, V)
P3  = pressure(0.85, V)

P1e, P2e, P3e = pressure2(1.15, rho), pressure2(1.0, rho), pressure2(0.85, rho)

fig = plt.figure(1)
ax1 = fig.add_subplot(311)
p1, = ax1.plot(V, P1)
p2, = ax1.plot(V, P2)
p3, = ax1.plot(V, P3)
ax1.set_ylabel(r'Pressure $\hat{P}$')
ax1.set_xlabel(r'Volume $\hat{V}$')
ax1.legend([p1,p2,p3], ["T=1.15", "T=1.0", "T=0.85"])
ax1.set_yscale('log')

ax3 = fig.add_subplot(312)
ax3.plot(P1, V); ax3.plot(P2, V); ax3.plot(P3, V)
ax3.set_xlabel(r'Pressure $\hat{P}$')
ax3.set_ylabel(r'Volume $\hat{V}$')
ax3.set_xscale('log')


ax2 = fig.add_subplot(313)
ax2.plot(P1e, rho)
ax2.plot(P2e, rho)
ax2.plot(P3e, rho)
ax2.set_ylabel(r'Density $\hat{\rho}$')
ax2.set_xlabel(r'Pressure $\hat{P}$')


plt.show()
