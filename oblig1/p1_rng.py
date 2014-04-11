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
noplot = True

# Generate sequence of X values
# where X = sum(r_i)
# w/ r_i = ran(-1,1)

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
    # Sequence of RVs:
    r.append(2 * random.rand(N[i]) - 1)

    # Variance?
    # Var(X) = E(X^2) - (E(X))^2

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

    # Histogram of the X-values (from largest sample)

    fig2 = plt.figure()
    ax1 = fig2.add_subplot(111)
    ax1.hist(r[-1])
    ax1.set_xlabel(r'RV value $X$')
    ax1.tick_params(axis='both', which='major', labelsize=18)
    ax1.tick_params(axis='both', which='minor', labelsize=14)
    plt.show()

# Print table with info
print('N \t Mean \t\t Squared mean \t Variance')
for i in xrange(len(N)):
    print('%i \t %g \t %g \t %g' % (N[i], Er[i], Er2[i], Var[i]))
