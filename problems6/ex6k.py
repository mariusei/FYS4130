# Exercise 6k

import matplotlib.pylab as plt
from numpy import *


def pressure(T, V):
    return 8.0 * T / float(3.0 * V - 1) - 3.0/float(V)**2

def pressure2(T, rho):
    return 8.0 * rho * T / (3.0 - rho) - 3.0 * rho**2

def gibbs_red(T, rho, P):
    return -3.0*rho - 8./3. * T * log(3./rho - 1.0) + float(P)/float(rho)

pressure = vectorize(pressure)
pressure2= vectorize(pressure2)
gibbs_red= vectorize(gibbs_red)

rho = linspace(0.2, 2.0, 500)
V   = 1./rho
P1  = pressure(0.9, V)
gibb= gibbs_red(0.9, rho, P1)

fig = plt.figure(1)
ax1 = fig.add_subplot(311)
p1, = ax1.plot(rho, P1)
ax1.plot(linspace(min(rho),max(rho), 500), ones(500)*0.647)
ax1.set_ylabel(r'Pressure $\hat{P}$')
ax1.set_xlabel(r'Density $\hat{\rho}$')
#ax1.set_xlabel(r'Volume $\hat{V}$')
#ax1.legend([p1,p2,p3], ["T=1.15", "T=1.0", "T=0.85"])
#ax1.set_yscale('log')

ax3 = fig.add_subplot(312)
ax3.plot(P1, V);# ax3.plot(P2, V); ax3.plot(P3, V)
ax3.plot(ones(500)*0.647, linspace(min(V),max(V), 500))
ax3.set_xlabel(r'Pressure $\hat{P}$')
ax3.set_ylabel(r'Volume $\hat{V}$')
ax3.set_xscale('log')


ax2 = fig.add_subplot(313)
ax2.plot(P1, gibb)
#ax2.plot(P2e, rho)
#ax2.plot(P3e, rho)
ax2.set_ylabel(r'Gibbs $\hat{g}$')
ax2.set_xlabel(r'Pressure $\hat{P}$')


plt.show()
