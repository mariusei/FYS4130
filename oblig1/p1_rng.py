# 
# FYS4130 Oblig 1
# Spring 2014
# Marius Berge Eide
#

# PART 1
# RANDOM NUMBERS

import matplotlib.pylab as plt
from numpy import *
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
noplot = False 

# 1.2.  HOW DOES THE VARIANCE SCALE WITH
#       THE NUMBER OF ELEMENTS?

# Number of RVs?
N   = 2**linspace(1,16,16) 
# Mean
Er  =    zeros(len(N))
# Mean of squares
Er2 = zeros(len(N))
# Variance
Var = zeros(len(N))
# Random number sequences
r = []

for i in xrange(len(N)):
    # Sequence of random numbers:
    r.append(2 * random.rand(N[i]) - 1)

    # Variance?
    # Var(x) = E(x^2) - (E(x))^2

    # Mean:
    Er[i] = mean(r[-1])

    # Mean of squares
    Er2[i] = mean(r[-1]*r[-1])

    # Variance
    Var[i] = Er2[i] - Er[i]**2

if not noplot:
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.plot(N, Var)
    ax1.set_xscale('log', basex=2)
    ax1.set_xlabel(r'Number of RVs: $N$')
    ax1.set_ylabel(r'Variance Var$(X)$ = E$(X^2)$ - E$(X)^2$')
    ax1.tick_params(axis='both', which='major', labelsize=18)
    ax1.tick_params(axis='both', which='minor', labelsize=14)
    plt.show()

# Print table with info
print('N \t Mean \t\t Squared mean \t Variance')
for i in xrange(len(N)):
    print('%i \t %g \t %g \t %g' % (N[i], Er[i], Er2[i], Var[i]))


# 1.3   HOW DOES A STATISTIC BEHAVE?
#       Repeat measurements k times

k = 200
N = 2**4

Er = zeros(k)
Er2= zeros(k)
Var= zeros(k)
r  = zeros(N)

for i in xrange(k):
    r       = 2 * random.rand(N) - 1
    Er[i]   = mean(r)
    Er2[i]  = mean(r*r)
    Var[i]  = Er2[i] - Er[i]*Er[i]


if not noplot:
    # Histogram of the X-values
    # Choose to consider mean

    fig2 = plt.figure()
    ax1 = fig2.add_subplot(111)
    ax1.hist(Er)
    ax1.set_xlabel(r'Mean of $X$')
    ax1.tick_params(axis='both', which='major', labelsize=18)
    ax1.tick_params(axis='both', which='minor', labelsize=14)
    plt.show()

