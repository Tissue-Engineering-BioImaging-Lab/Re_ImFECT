# -*- coding: utf-8 -*-

"""
@author: Joshua J.A. Poole

Calculates 16 texture features from Gray Level Size Zone Matrix (GLSZM).

INPUT: GLSZM form of Numpy array.
OUTPIT: Features calculates from GLRLM in form of Dict.

ARGUMENTS: 
    glszm - Gray Level Size Zone Matrix.
    numPixels - Total number of pixels found in image. 
    
"""

import math


def calcGLSZMMetrics(glszm, numPixels):

    # Initialized Parameters

    numGray = glszm.shape[0]
    numSize = glszm.shape[1]
    numZones = glszm.sum()

    glszm_norm = glszm/numZones

    rowTotal = 0
    colTotal = 0

    avgGray = 0
    avgSize = 0

    arbitSmall = 1e-22

    # Create Dict to store metrics

    glszmMetrics = {
        "GLSZM - Small Area Emphasis": 0,
        "GLSZM - Large Area Emphasis": 0,
        "GLSZM - Low Gray Level Zone Emphasis": 0,
        "GLSZM - High Gray Level Zone Emphasis": 0,
        "GLSZM - Small Area Low Gray Level Zone Emphasis": 0,
        "GLSZM - Large Area Low Gray Level Zone Emphasis": 0,
        "GLSZM - Small Area High Gray Level Zone Emphasis": 0,
        "GLSZM - Large Area High Gray Level Zone Emphasis": 0,
        "GLSZM - Gray Level Variance": 0,
        "GLSZM - Gray Level Non-Uniformity": 0,
        "GLSZM - Gray Level Non-Uniformity Normalized": 0,
        "GLSZM - Size Zone Variance": 0,
        "GLSZM - Size Zone Non-Uniformity": 0,
        "GLSZM - Size Zone Non-Uniformity Normalized": 0,
        "GLSZM - Size Zone Entropy": 0,
        "GLSZM - Size Zone Percentage": 0
    }

    # Calculate average for gray levels

    for i in range(0, numGray):
        for j in range(0, numSize):

            avgGray += glszm_norm[i][j]*(i+1)

    # Calculate average for size zones

    for i in range(0, numGray):
        for j in range(0, numSize):

            avgSize += glszm_norm[i][j]*(j+1)

    # Calculate metrics

    for i in range(0, numGray):
        for j in range(0, numSize):

            glszmValue = glszm[i][j]
            glszmNormValue = glszm_norm[i][j]

            glszmMetrics["GLSZM - Small Area Emphasis"] \
                += glszmValue/((j+1)**2)

            glszmMetrics["GLSZM - Large Area Emphasis"] \
                += glszmValue*((j+1)**2)

            glszmMetrics["GLSZM - Low Gray Level Zone Emphasis"] \
                += glszmValue/((i+1)**2)

            glszmMetrics["GLSZM - High Gray Level Zone Emphasis"] \
                += glszmValue*((i+1)**2)

            glszmMetrics["GLSZM - Small Area Low Gray Level Zone Emphasis"] \
                += glszmValue/(((i+1)**2)*((j+1)**2))

            glszmMetrics["GLSZM - Small Area High Gray Level Zone Emphasis"] \
                += (glszmValue*((i+1)**2))/((j+1)**2)

            glszmMetrics["GLSZM - Large Area Low Gray Level Zone Emphasis"] \
                += (glszmValue*((j+1)**2))/((i+1)**2)

            glszmMetrics["GLSZM - Large Area High Gray Level Zone Emphasis"] \
                += glszmValue*(((i+1)**2)*((j+1)**2))

            glszmMetrics["GLSZM - Gray Level Variance"] \
                += glszmNormValue*(abs(((i+1)-avgGray))**2)

            glszmMetrics["GLSZM - Size Zone Variance"] \
                += glszmNormValue*(abs(((j+1)-avgSize))**2)

            glszmMetrics["GLSZM - Size Zone Entropy"] \
                -= glszmNormValue*math.log2(glszmNormValue+arbitSmall)

            rowTotal += glszmValue

        glszmMetrics["GLSZM - Gray Level Non-Uniformity"] += rowTotal**2

        rowTotal = 0

    for j in range(0, numSize):
        for i in range(0, numGray):

            colTotal += glszm[i][j]

        glszmMetrics["GLSZM - Size Zone Non-Uniformity"] += colTotal**2

        colTotal = 0

    glszmMetrics["GLSZM - Small Area Emphasis"] /= numZones

    glszmMetrics["GLSZM - Large Area Emphasis"] /= numZones

    glszmMetrics["GLSZM - Low Gray Level Zone Emphasis"] /= numZones

    glszmMetrics["GLSZM - High Gray Level Zone Emphasis"] /= numZones

    glszmMetrics["GLSZM - Small Area Low Gray Level Zone Emphasis"] /= numZones

    glszmMetrics["GLSZM - Small Area High Gray Level Zone Emphasis"] /= numZones

    glszmMetrics["GLSZM - Large Area Low Gray Level Zone Emphasis"] /= numZones

    glszmMetrics["GLSZM - Large Area High Gray Level Zone Emphasis"] /= numZones

    glszmMetrics["GLSZM - Gray Level Non-Uniformity"] /= numZones

    glszmMetrics["GLSZM - Gray Level Non-Uniformity Normalized"] = \
        glszmMetrics["GLSZM - Gray Level Non-Uniformity"]/numZones

    glszmMetrics["GLSZM - Size Zone Non-Uniformity"] /= numZones

    glszmMetrics["GLSZM - Size Zone Non-Uniformity Normalized"] = \
        glszmMetrics["GLSZM - Size Zone Non-Uniformity"]/numZones

    glszmMetrics["GLSZM - Size Zone Percentage"] = numZones/numPixels

    return glszmMetrics
