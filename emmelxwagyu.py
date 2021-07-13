import numpy as np

nInst=100
currentPos = np.zeros(nInst)

# Dummy algorithm to demonstrate function format.
def getMyPosition (prcSoFar):
    global currentPos
    (nins,nt) = prcSoFar.shape # (number of instruments, number of days)
    mpos = np.zeros(nins)
    pos_mom = 0                 # counts total positive momentum
    neg_mom = 0                 # Counts total negative momentum

    ###### 14 DAY MOVING AVERAGE
    mov_avg = np.zeros(nins)    # Create an array of zeros to store moving averages  
    tot_wind = np.zeros(nins)   # Summation of price over the time window
    prc_std = np.zeros(nins)    # Price std
    upper_band = np.zeros(nins) # Array for Upper band - +2 std
    lower_band = np.zeros(nins) # Array for Upper band - -2 std
    window_size = 10            # Parameter for window size
    BB_val = np.zeros(nins)     # Array for BB values
    BB_pos = 0                  # Counts total positive BB (Unused)
    BB_neg = 0                  # Counts total negative BB (Unused)

    for i in range(100):
        for m in range(1, window_size+1):
            tot_wind[i] += prcSoFar[i,-m]                               # Summation of price over time window
        mov_avg[i] = tot_wind[i] / window_size                          # moving average calculation
        prc_std[i] = np.std(prcSoFar[i,:])                              # price std calculation
        upper_band[i] = mov_avg[i] + 2 * prc_std[i]                     # upper band calculation
        lower_band[i] = mov_avg[i] - 2 * prc_std[i]                     # lower band calculation
        BB_val[i] = (prcSoFar[i,-1] - mov_avg[i])/(2 * prc_std[i])      # bb calculation
        if BB_val[i] > 0:
            BB_pos += BB_val[i]                                         # bb_pos counter (unused)
        else:
            BB_neg += BB_val[i]                                         # bb_neg counter (unused)

#    cpos = np.zeros(nins)
#    for i in range(100):
#        if BB_val[i] > 1:
#            cpos[i] = -(BB_val[i]/BB_neg) * 5000  # normalise and scale by 5,000
#        elif BB_val[i] < 0:
#            cpos[i] = (BB_val[i]/BB_neg) * 5000   # normalise and scale by 5,000



    ###### Momentum #######
    mom = np.zeros(nins)                                # Array on zeros
    for i in range(100):                                # For loop over 0 to 99
        mom[i] = (prcSoFar[i,-1]/mov_avg[i]) - 1        # Calculation of momentum
        if mom[i] > 0:                                  # Calculate the total "positive" and "negative" momentum
            pos_mom += mom[i]
        else:
            neg_mom += mom[i]   

    ####### Positions #######
    for i in range(100):                                # Another loop over 0 to 99
        if mom[i] > 0 and BB_val[i] > 0:                # Sell criteria
            mpos[i] = int(-(mom[i]/pos_mom) * 10000)    # normalise and scale by 10,000
        elif mom[i] < 0 and BB_val[i] < 0:              # Buy Criteria
            mpos[i] = int((mom[i]/neg_mom) * 10000)     # normalise and scale by 10,000
    
    currentPos = mpos
    return currentPos