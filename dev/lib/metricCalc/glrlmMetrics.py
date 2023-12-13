# -*- coding: utf-8 -*-

"""
@author: Joshua J.A. Poole

Calculates 16 texture features from Gray Level Run Length Matrix (GLRLM).

INPUT: GLRLM form of Numpy array.
OUTPIT: Features calculates from GLRLM in form of Dict.

ARGUMENTS: 
    glrlm - Gray Level Run Length Matrix.
    numPixels - Total number of pixels found in image. 
    
"""

import math

def calcGLRLMMetrics(glrlm, numPixels):

    # Initialized Parameters
    
    numGray = glrlm.shape[0]
    numLength = glrlm.shape[1]
    numRuns = glrlm.sum()
    
    glrlm_norm = glrlm/numRuns
    
    rowTotal = 0
    colTotal = 0
    
    avgGray = 0
    avgLength = 0
    
    arbitSmall = 1e-22
    
    # Create Dict to store metrics
    
    glrlmMetrics = {
            "GLRLM - Short Run Emphasis" : 0,
            "GLRLM - Long Run Emphasis" : 0,
            "GLRLM - Low Gray Level Run Emphasis" : 0,            
            "GLRLM - High Gray Level Run Emphasis" : 0,       
            "GLRLM - Short Run Low Gray Emphasis" : 0,
            "GLRLM - Short Run High Gray Emphasis" : 0,
            "GLRLM - Long Run Low Gray Emphasis" : 0,
            "GLRLM - Long Run High Gray Emphasis" : 0,
            "GLRLM - Gray Level Variance" : 0,  
            "GLRLM - Gray Level Non-Uniformity" : 0,
            "GLRLM - Gray Level Non-Uniformity Normalized" : 0,
            "GLRLM - Run Variance" : 0,
            "GLRLM - Run Length Non-Uniformity" : 0,
            "GLRLM - Run Length Non-Uniformity Normalized" : 0,
            "GLRLM - Run Length Percentage" : 0,
            "GLRLM - Run Entropy" : 0
        }
    
    # Calculate average for gray levels
    
    for i in range(0, numGray):
        for j in range(0, numLength):
        
            avgGray += glrlm_norm[i][j]*(i+1)
            
    # Calculate average for size zones
            
    for i in range(0, numGray):
        for j in range(0, numLength):
        
            avgLength += glrlm_norm[i][j]*(j+1)
    
    # Calculate metrics
    
    for i in range(0, numGray):
        for j in range(0, numLength):
            
            glrlmMetrics["GLRLM - Short Run Emphasis"] += \
                glrlm[i][j]/((j+1)**2)
            
            glrlmMetrics["GLRLM - Long Run Emphasis"] += \
                glrlm[i][j]*((j+1)**2)
            
            glrlmMetrics["GLRLM - Low Gray Level Run Emphasis"] += \
                glrlm[i][j]/((i+1)**2)
            
            glrlmMetrics["GLRLM - High Gray Level Run Emphasis"] += \
                glrlm[i][j]*((i+1)**2)
            
            glrlmMetrics["GLRLM - Short Run Low Gray Emphasis"] += \
                glrlm[i][j]/(((i+1)**2)*((j+1)**2))
            
            glrlmMetrics["GLRLM - Short Run High Gray Emphasis"] += \
                (glrlm[i][j]*((i+1)**2))/((j+1)**2)
            
            glrlmMetrics["GLRLM - Long Run Low Gray Emphasis"] += \
                (glrlm[i][j]*((j+1)**2))/((i+1)**2)
            
            glrlmMetrics["GLRLM - Long Run High Gray Emphasis"] += \
                glrlm[i][j]*(((i+1)**2)*((j+1)**2))
                        
            glrlmMetrics["GLRLM - Gray Level Variance"] += \
                glrlm_norm[i][j]*(((i+1)-avgGray)*((i+1)-avgGray))
            
            glrlmMetrics["GLRLM - Run Variance"] += \
                glrlm_norm[i][j]*(((j+1)-avgLength)*((j+1)-avgLength))
            
            glrlmMetrics["GLRLM - Run Entropy"] -= \
                glrlm_norm[i][j]*math.log2(glrlm_norm[i][j]+arbitSmall)
            
            rowTotal += glrlm[i][j]
        
        glrlmMetrics["GLRLM - Gray Level Non-Uniformity"] += rowTotal**2
        
        rowTotal = 0
        
    for j in range(0, numLength):
        for i in range(0, numGray):
            
            colTotal += glrlm[i][j]
            
        glrlmMetrics["GLRLM - Run Length Non-Uniformity"] += colTotal**2
        
        colTotal = 0
        
    glrlmMetrics["GLRLM - Short Run Emphasis"] /= numRuns
    
    glrlmMetrics["GLRLM - Long Run Emphasis"] /= numRuns
    
    glrlmMetrics["GLRLM - Low Gray Level Run Emphasis"] /= numRuns
    
    glrlmMetrics["GLRLM - High Gray Level Run Emphasis"] /= numRuns
    
    glrlmMetrics["GLRLM - Short Run Low Gray Emphasis"] /= numRuns
    
    glrlmMetrics["GLRLM - Short Run High Gray Emphasis"] /= numRuns
    
    glrlmMetrics["GLRLM - Long Run Low Gray Emphasis"] /= numRuns
    
    glrlmMetrics["GLRLM - Long Run High Gray Emphasis"] /= numRuns
    
    glrlmMetrics["GLRLM - Gray Level Non-Uniformity"] /= numRuns
    
    glrlmMetrics["GLRLM - Gray Level Non-Uniformity Normalized"] \
        = glrlmMetrics["GLRLM - Gray Level Non-Uniformity"]/numRuns
    
    glrlmMetrics["GLRLM - Run Length Non-Uniformity"] /= numRuns
    
    glrlmMetrics["GLRLM - Run Length Non-Uniformity Normalized"] \
        = glrlmMetrics["GLRLM - Run Length Non-Uniformity"]/numRuns
    
    glrlmMetrics["GLRLM - Run Length Percentage"] = numRuns/numPixels
    
    return glrlmMetrics
