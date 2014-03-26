# 
# FYS4130 Oblig 1
# Spring 2014
# Marius Berge Eide
#

# PART 1
# RANDOM NUMBERS

import matplotlib.pylab as plt
from numpy import *

# Generate sequence of X values
# where X = sum(r_i)
# w/ r_i = ran(-1,1)

r = 2 * random.rand(5) - 1
print r 
