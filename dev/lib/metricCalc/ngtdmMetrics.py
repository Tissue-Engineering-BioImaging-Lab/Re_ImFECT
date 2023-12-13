# -*- coding: utf-8 -*-

"""
@author: Joshua J.A. Poole

Calculates 5 texture features from Neighbouring Gray Tone Difference Matrix (NGTDM).

INPUT: NGTDM form of Numpy array.
OUTPIT: Features calculates from GLRLM in form of Dict.

ARGUMENTS: 
    ngtdm - Gray Level Dependence Matrix.
    
"""

# import math


def calcNGTDMMetrics(ngtdm):

    # Initialized Parameters

    numGray = ngtdm.shape[0]

    numGrayNonZero = 0
    numPixels = 0

    ngtdmCoarseness = 0

    ngtdmContrast1 = 0
    ngtdmContrast2 = 0

    ngtdmBusyness = 0

    ngtdmStrength = 0

    # Create Dict to store metrics

    ngtdmMetrics = {
        "NGTDM - Coarseness": 0,
        "NGTDM - Contrast": 0,
        "NGTDM - Busyness": 0,
        "NGTDM - Complexity": 0,
        "NGTDM - Strength": 0
    }

    numGrayLevels = range(0, numGray)

    # Calculate average for gray levels

    for i in numGrayLevels:

        p_i = ngtdm[i][1]
        s_i = ngtdm[i][2]

        ngtdmCoarseness += p_i*s_i

        ngtdmContrast2 += s_i

        numPixels += ngtdm[i][0]

        if p_i != 0:
            numGrayNonZero += 1

        for j in numGrayLevels:

            p_j = ngtdm[j][1]
            s_j = ngtdm[j][2]

            if p_i != 0 and p_j != 0:
                ngtdmContrast1 += p_i*p_j*(abs(i-j)**2)

                ngtdmBusyness += abs(((i+1)*p_i)-((j+1)*p_j))

                ngtdmMetrics["NGTDM - Complexity"] += (abs(i-j) *
                                                       (((p_i*s_i)+(p_j*s_j)) /
                                                        (p_i+p_j)))

                ngtdmStrength += (p_i+p_j)*(abs(i-j)**2)

    ngtdmMetrics["NGTDM - Coarseness"] = 1/ngtdmCoarseness

    ngtdmMetrics["NGTDM - Contrast"] = ((1/(numGrayNonZero*(numGrayNonZero-1)))
                                        * ngtdmContrast1*(1/numPixels) *
                                        ngtdmContrast2)

    ngtdmMetrics["NGTDM - Busyness"] = ngtdmCoarseness/ngtdmBusyness

    ngtdmMetrics["NGTDM - Complexity"] /= numPixels

    ngtdmMetrics["NGTDM - Strength"] = ngtdmStrength/ngtdmContrast2

    return ngtdmMetrics
