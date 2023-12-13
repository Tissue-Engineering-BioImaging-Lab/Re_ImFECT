# -*- coding: utf-8 -*-
"""
@author: Joshua J.A. Poole

Calculates 25 texture features from Gray Level Cooccurance Matrix (GLCM).

INPUT: GLCM form of Numpy array.
OUTPIT: Features calculates from GLCM in form of Dict.

ARGUMENTS: 
    glcm - Gray Level Cooccurance Matrix.
    
"""

import math
import numpy as np


def calcGLCMMetrics(glcm):

    # Initialize variables
    d_0 = 1e-8  # avoid division by zero
    glcmNormValue = 0

    mu_x = 0
    mu_y = 0

    sigma_p_x = 0
    sigma_p_y = 0

    HX = 0
    HY = 0
    HXY = 0
    HXY1 = 0
    HXY2 = 0

    # Arbitarily Small Number

    arbitSmall = 1e-22

    # Create Dict to store metrics

    glcmMetrics = {
        "GLCM - Autocorrelation": 0,
        "GLCM - Cluster Prominence": 0,
        "GLCM - Cluster Shade": 0,
        "GLCM - Cluster Tendency": 0,
        "GLCM - Contrast": 0,
        "GLCM - Correlation": 0,
        "GLCM - Difference Average": 0,
        "GLCM - Difference Variance": 0,
        "GLCM - Difference Entropy": 0,
        "GLCM - Joint Average": 0,
        "GLCM - Joint Energy": 0,
        "GLCM - Joint Entropy": 0,
        "GLCM - Homogeneity": 0,
        "GLCM - Informational Measure of Correlation 1": 0,
        "GLCM - Informational Measure of Correlation 2": 0,
        "GLCM - Maximal Correlation Coefficient": 0,
        "GLCM - Inverse Difference Moment": 0,
        "GLCM - Inverse Difference Moment Normalized": 0,
        "GLCM - Inverse Difference": 0,
        "GLCM - Inverse Difference Normalized": 0,
        "GLCM - Inverse Variance": 0,
        "GLCM - Maximum Probability": 0,
        "GLCM - Sum Average": 0,
        "GLCM - Sum Entropy": 0,
        "GLCM - Sum Of Squares": 0
    }

    # Extract Parameters from GLCM

    numGray = glcm.shape[0]
    glcm_norm = glcm/(glcm.sum()+1e-8)

    p_x = glcm_norm.sum(1)
    p_y = glcm_norm.sum(0)

    p_x_plus_y = np.zeros(2*numGray-1)
    p_x_minus_y = np.zeros(numGray)

    Q = np.zeros([numGray, numGray])

    numGrayLevels = range(0, numGray)
    numGrayLevelsSum = range(0, 2*numGray-1)

    # Calculate parameters for use in further calculations.

    for i in numGrayLevels:

        mu_x += (i+1)*p_x[i]
        mu_y += (i+1)*p_y[i]
    for i in numGrayLevels:

        sigma_p_x += (((i+1)-mu_x)*((i+1)-mu_x))*p_x[i]
        sigma_p_y += (((i+1)-mu_y)*((i+1)-mu_y))*p_y[i]

    sigma_p_x = math.sqrt(sigma_p_x)
    sigma_p_y = math.sqrt(sigma_p_y)

    for i in numGrayLevels:

        HX -= p_x[i]*math.log2(p_x[i]+arbitSmall)
        HY -= p_y[i]*math.log2(p_y[i]+arbitSmall)

        for j in numGrayLevels:

            glcmNormValue = glcm_norm[i][j]

            glcmMetrics["GLCM - Autocorrelation"] += glcmNormValue*(i+1)*(j+1)

            glcmMetrics["GLCM - Joint Average"] += glcmNormValue*(i+1)

            glcmMetrics["GLCM - Cluster Prominence"] += (
                ((i+1)+(j+1)-mu_x-mu_y) *
                ((i+1)+(j+1)-mu_x-mu_y) *
                ((i+1)+(j+1)-mu_x-mu_y) *
                ((i+1)+(j+1)-mu_x-mu_y)
            ) * glcmNormValue

            glcmMetrics["GLCM - Cluster Shade"] += (
                (((i+1)+(j+1)-mu_x-mu_y)*((i+1)+(j+1)-mu_x-mu_y)
                 * ((i+1)+(j+1)-mu_x-mu_y))*glcmNormValue
            )

            glcmMetrics["GLCM - Cluster Tendency"] += (
                (((i+1)+(j+1)-mu_x-mu_y)*((i+1)+(j+1)-mu_x-mu_y))*glcmNormValue
            )

            glcmMetrics["GLCM - Contrast"] += (
                (((i+1)-(j+1))*((i+1)-(j+1)))*glcmNormValue
            )

            glcmMetrics["GLCM - Correlation"] += (
                glcmNormValue *
                (((i+1)-mu_x)/(sigma_p_x+d_0)) *
                (((j+1)-mu_x)/(sigma_p_x+d_0))
            )

            glcmMetrics["GLCM - Joint Energy"] += (
                glcmNormValue**2
            )

            glcmMetrics["GLCM - Joint Entropy"] -= (
                glcmNormValue*math.log2(glcmNormValue + arbitSmall)
            )

            glcmMetrics["GLCM - Homogeneity"] += (
                glcmNormValue/(1+abs((i+1)-(j+1))+d_0)
            )

            glcmMetrics["GLCM - Sum Of Squares"] += (
                (((i+1) - mu_x)*((i+1) - mu_x))*glcmNormValue
            )

            p_x_plus_y[i+j] += glcmNormValue
            p_x_minus_y[abs(i-j)] += glcmNormValue

            HXY -= glcmNormValue*math.log2(
                glcmNormValue + arbitSmall
            )
            HXY1 -= glcmNormValue*math.log2(
                p_x[i]*p_y[j] + arbitSmall
            )
            HXY2 -= p_x[i]*p_y[j]*math.log2(
                p_x[i]*p_y[j] + arbitSmall
            )

            for k in numGrayLevels:

                Q[i][j] += (
                    (glcm_norm[i][k]*glcm_norm[j][k]) /
                    (p_x[i]*p_y[k]+arbitSmall)+d_0
                )

    for k in numGrayLevels:

        glcmMetrics["GLCM - Difference Average"] += k*p_x_minus_y[k]

    for k in numGrayLevels:

        glcmMetrics["GLCM - Difference Variance"] += (
            ((k-glcmMetrics["GLCM - Difference Average"])**2)*p_x_minus_y[k]
        )

        glcmMetrics["GLCM - Difference Entropy"] -= (
            p_x_minus_y[k]*math.log2(p_x_minus_y[k]+arbitSmall)
        )

        glcmMetrics["GLCM - Inverse Difference Moment"] += (
            p_x_minus_y[k]/(1+(k**2)+d_0)
        )

        glcmMetrics["GLCM - Inverse Difference Moment Normalized"] += (
            p_x_minus_y[k] / (1+((k*k)/numGray*numGray)+d_0)
        )

        glcmMetrics["GLCM - Inverse Difference"] += p_x_minus_y[k]/(1+k)

        glcmMetrics["GLCM - Inverse Difference Normalized"] += (
            p_x_minus_y[k]/(1+(k/numGray)+d_0)
        )

        if k == 0:
            continue

        glcmMetrics["GLCM - Inverse Variance"] += p_x_minus_y[k]/(k**2)

    for k in numGrayLevelsSum:

        glcmMetrics["GLCM - Sum Average"] += (
            p_x_plus_y[k]*(k+2)
        )

        glcmMetrics["GLCM - Sum Entropy"] -= (
            p_x_plus_y[k]*math.log2(p_x_plus_y[k]+arbitSmall)
        )

    if HX != 0 or HY != 0:

        glcmMetrics["GLCM - Informational Measure of Correlation 1"] = (
            (HXY - HXY1)/(max(HX, HY)+d_0)
        )

    if HXY <= HXY2:

        glcmMetrics["GLCM - Informational Measure of Correlation 2"] = (
            math.sqrt(1-math.exp(-2*(HXY2-HXY)))
        )

    eigenvalues = np.sort(np.linalg.eigvals(Q).real)
    secondLargestEigen = eigenvalues[-2]

    glcmMetrics["GLCM - Maximal Correlation Coefficient"] = (
        math.sqrt(secondLargestEigen)
    )

    glcmMetrics["GLCM - Maximum Probability"] = (
        glcm_norm.max()
    )

    return glcmMetrics
