#!/usr/bin/env python

# RENAME THIS FILE WITH YOUR TEAM NAME.

import numpy as np

nInst=100
currentPos = np.zeros(nInst)

# Dummy algorithm to demonstrate function format.
def getMyPosition (prcSoFar):
    global currentPos
    (nins,nt) = prcSoFar.shape # (number of instruments, number of days)
    #print(nins)
    change = np.zeros(nins)
    rpos = np.zeros(nins)
    pos = 0  				# counts total positive movement
    neg = 0					# counts total negative movement
    for i in range(1,100):
    	change[i] = prcSoFar[i,-1] - prcSoFar[i, -2]; # Recent price movement
    	if change[i] > 0:	
    		pos = pos + change[i]
    	else:
    		neg = neg + change[i]	
    #print(pos, neg)
    #print(change)
    for i in range(1,100):
    	if change[i] > 0:
    		rpos[i] = -(change[i]/pos) * 10000 	# normalise and scale by 10,000
    	else:
    		rpos[i] = (change[i]/neg) * 10000	# normalise and scale by 10,000
    	
    #print("this:", prcSoFar[2,-1], prcSoFar[2,-2])
    #rpos = np.array([int(x) for x in 1000 * np.random.randn(nins)])
    #print(rpos)

    currentPos += rpos

    # The algorithm must return a vector of integers, indicating the position of each stock.
    # Position = number of shares, and can be positve or negative depending on long/short position.
    return currentPos
