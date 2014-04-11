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
N = 100 

Tot= zeros(k)
Er = zeros(k)
Er2= zeros(k)
Var= zeros(k)
r  = zeros(N)

A = 4.
B = 100.
sigmasq = (A / tanh(A)  - 1.) * B**2 / A**2 * sinh(A)**2
an_mean = B/A * sinh(A)

print("Analytical mean: %g" % an_mean)

for i in xrange(k):
    y       = 2 * random.rand(N) - 1
    x       = B * exp(A*y)
    r       = 1./( 2*A*x )
    Tot[i]  = sum(r)
    Er[i]   = mean(r)
    Er2[i]  = mean(r*r)
    Var[i]  = Er2[i] - Er[i]*Er[i]


if not noplot:
    # Histogram of the X-values
    yvals = linspace(B*exp(-A), B*exp(A))
#    gaus  = 1./(2*pi*N*sigmasq) * exp( -(yvals - an_mean)**2 / (2*N*sigmasq) )
    gaus  = 1./(2*pi*sigmasq) * exp( -(yvals - an_mean)**2 / (2*sigmasq) )

    fig2 = plt.figure()
    ax1 = fig2.add_subplot(111)
    nhist, binhist, patchist = ax1.hist(Er, 100, weights=ones_like(Er)/k)
#    ax1.hist(Tot)
#    ax1.plot(yvals, gaus)
    ax1.set_xlabel(r'Mean of $X$')
    ax1.tick_params(axis='both', which='major', labelsize=18)
    ax1.tick_params(axis='both', which='minor', labelsize=14)
    plt.show()

# Compare theoretical N<Dx^2> to computed <DX^2>
# Theoretical
print "Theoretical N<Dx^2> =", N*sigmasq
# Computed
print "Computed <DX^2> =", mean(Var) 

# Other statistics
print "Mean of statistic mean: ", mean(Er)

# Create running average of the means

initloc  = 5
finalloc = len(nhist)-5
runavg   = zeros(len(nhist))
#Er = sort(Er)

for i in xrange(5,len(nhist)-5):
    runavg[i] = mean(nhist[i-5:i+4])

plt.plot(binhist[0:-1],runavg)
plt.xlabel('Mean of $X$')
plt.show()

