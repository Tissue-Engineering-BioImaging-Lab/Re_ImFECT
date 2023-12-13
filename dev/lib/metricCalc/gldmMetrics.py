# -*- coding: utf-8 -*-

"""
@author: Joshua J.A. Poole

Calculates 15 texture features from Gray Level Dependence Matrix (GLDM).

INPUT: GLDM form of Numpy array.
OUTPIT: Features calculates from GLDM in form of Dict.

ARGUMENTS: 
    gldm - Gray Level Dependence Matrix.
    
"""

import math

def calcGLDMMetrics(gldm):

    # Initialized Parameters
    
    numGray = gldm.shape[0]
    numSize = gldm.shape[1]
    numZones = gldm.sum()
    
    gldm_norm = gldm/numZones
    
    rowTotal = 0
    colTotal = 0
    
    avgGray = 0
    avgSize = 0
    
    arbitSmall = 1e-22
    
    # Create Dict to store metrics
    
    gldmMetrics = {
        "GLDM - Small Dependence Emphasis" : 0,
        "GLDM - Large Dependence Emphasis" : 0,
        "GLDM - Low Gray Level Emphasis" : 0,         
        "GLDM - High Gray Level Emphasis" : 0,
        "GLDM - Small Dependence Low Gray Level Emphasis" : 0,
        "GLDM - Large Dependence Low Gray Level Emphasis" : 0,
        "GLDM - Small Dependence High Gray Level Emphasis" : 0,
        "GLDM - Large Dependence High Gray Level Emphasis" : 0,
        "GLDM - Gray Level Variance" : 0,
        "GLDM - Gray Level Non-Uniformity" : 0,
        "GLDM - Gray Level Non-Uniformity Normalized" : 0,
        "GLDM - Dependence Variance" : 0,
        "GLDM - Dependence Non-Uniformity" : 0,
        "GLDM - Dependence Non-Uniformity Normalized" : 0,
        "GLDM - Dependence Entropy" : 0
        }
    
    # Calculate average for gray levels
    
    for i in range(0, numGray):
        for j in range(0, numSize):
        
            avgGray += gldm_norm[i][j]*(i+1)
            
    # Calculate average for size zones
            
    for i in range(0, numGray):
        for j in range(0, numSize):
        
            avgSize += gldm_norm[i][j]*(j+1)
    
    # Calculate metrics
    
    for i in range(0, numGray):
        for j in range(0, numSize):
            
            gldmValue = gldm[i][j]
            gldmNormValue = gldm_norm[i][j]
            
            gldmMetrics["GLDM - Small Dependence Emphasis"] += \
                gldmValue/((j+1)**2)
            
            gldmMetrics["GLDM - Large Dependence Emphasis"] += \
                gldmValue*((j+1)**2)
            
            gldmMetrics["GLDM - Low Gray Level Emphasis"] += \
                gldmValue/((i+1)**2)
            
            gldmMetrics["GLDM - High Gray Level Emphasis"] += \
                gldmValue*((i+1)**2)
            
            gldmMetrics["GLDM - Small Dependence Low Gray Level Emphasis"] += \
                gldmValue/(((i+1)**2)*((j+1)**2))
            
            gldmMetrics["GLDM - Small Dependence High Gray Level Emphasis"] +=\
                (gldmValue*((i+1)**2))/((j+1)**2)
            
            gldmMetrics["GLDM - Large Dependence Low Gray Level Emphasis"] += \
                (gldmValue*((j+1)**2))/((i+1)**2)
            
            gldmMetrics["GLDM - Large Dependence High Gray Level Emphasis"] +=\
                gldmValue*(((i+1)**2)*((j+1)**2))
                        
            gldmMetrics["GLDM - Gray Level Variance"] += \
                gldmNormValue*(((i+1)-avgGray)*((i+1)-avgGray))
            
            gldmMetrics["GLDM - Dependence Variance"] += \
                gldmNormValue*(((j+1)-avgSize)*((j+1)-avgGray))
            
            gldmMetrics["GLDM - Dependence Entropy"] -= \
                gldmNormValue*math.log2(gldmNormValue+arbitSmall)
            
            rowTotal += gldmValue
        
        gldmMetrics["GLDM - Gray Level Non-Uniformity"] += rowTotal**2
        
        rowTotal = 0
        
    for j in range(0, numSize):
        for i in range(0, numGray):
            
            colTotal += gldm[i][j]
            
        gldmMetrics["GLDM - Dependence Non-Uniformity"] += colTotal**2
        
        colTotal = 0
        
    gldmMetrics["GLDM - Small Dependence Emphasis"] /= numZones
    
    gldmMetrics["GLDM - Large Dependence Emphasis"] /= numZones
    
    gldmMetrics["GLDM - Low Gray Level Emphasis"] /= numZones
    
    gldmMetrics["GLDM - High Gray Level Emphasis"] /= numZones
    
    gldmMetrics["GLDM - Small Dependence Low Gray Level Emphasis"] /= numZones
    
    gldmMetrics["GLDM - Small Dependence High Gray Level Emphasis"] /= numZones
    
    gldmMetrics["GLDM - Large Dependence Low Gray Level Emphasis"] /= numZones
    
    gldmMetrics["GLDM - Large Dependence High Gray Level Emphasis"] /= numZones
    
    gldmMetrics["GLDM - Gray Level Non-Uniformity"] /= numZones
    
    gldmMetrics["GLDM - Gray Level Non-Uniformity Normalized"] \
        = gldmMetrics["GLDM - Gray Level Non-Uniformity"]/numZones
    
    gldmMetrics["GLDM - Dependence Non-Uniformity"] /= numZones
    
    gldmMetrics["GLDM - Dependence Non-Uniformity Normalized"] \
        = gldmMetrics["GLDM - Dependence Non-Uniformity"]/numZones
    
    return gldmMetrics
