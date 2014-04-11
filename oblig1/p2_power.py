# 
# FYS4130 Oblig 1
# Spring 2014
# Marius Berge Eide
#

# PART 2
# POWER LAW DISTRIBUTED RANDOM NUMBERS 

import matplotlib.pylab as plt
from numpy import *
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
noplot = False 


# 2.6   HOW DOES A STATISTIC BEHAVE?
#       Repeat measurements k times

k = 200
N = 1000 

Er = zeros(k)
Er2= zeros(k)
Var= zeros(k)
r  = zeros(N)

A = 1.
B = 1.
sigmasq = (A / tanh(A)  - 1.) * B**2 / A**2 * sinh(A)**2
an_mean = B/A * sinh(A)

print("Analytical mean: %g" % an_mean)

for i in xrange(k):
    y       = 2 * random.rand(N) - 1
    x       = B * exp(A*y)
    r       = 1./( 2*A*x )
    Er[i]   = mean(r)
    Er2[i]  = mean(r*r)
    Var[i]  = Er2[i] - Er[i]*Er[i]


if not noplot:
    # Histogram of the X-values
    yvals = linspace(B*exp(-A), B*exp(A))
    gaus  = 1./(2*pi*sigmasq) * exp( -(yvals - an_mean)**2 / (2*sigmasq) )

    fig2 = plt.figure()
    ax1 = fig2.add_subplot(111)
    ax1.hist(Er, weights=ones_like(Er)/k)
    ax1.plot(yvals, gaus)
    ax1.set_xlabel(r'Mean of $X$')
    ax1.tick_params(axis='both', which='major', labelsize=18)
    ax1.tick_params(axis='both', which='minor', labelsize=14)
    plt.show()

