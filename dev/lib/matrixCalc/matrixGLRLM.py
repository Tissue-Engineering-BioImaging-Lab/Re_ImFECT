# -*- coding: utf-8 -*-
"""
@author: Joshua J.A. Poole

Constructs Gray-Level Run Length Matrix (GLRLM) from image.

INPUT: Image in form of Numpy array.
OUTPIT: GLRLM from image in form of Numpy array.

ARGUMENTS: 
    arr - Image in form of array.
    Angle - Angle of calculation (0, 45, 90, or 135).
    bitDepth - Bitdepth of image. Determines size of GLDM.
    ignoreBackground - If true, ignores pixels with value 0. Prevents matrices from being too large. (Default = True)
"""

import numpy as np


def calc_glrlm(arr, angle, bitDepth, ignoreBackground=True):

    numIntensities = 2**bitDepth
    longestAxisLength = max(arr.shape[0], arr.shape[1])

    runLength = 0

    glrlm = np.zeros((numIntensities, longestAxisLength))

# Different angles require different comparisons.
# Decides which path to take, depending on direction required.

    if angle == 0:  # 0 Degrees. Compare pixels to Left and Right.

        for i in range(0, arr.shape[0]):

            runLength = 0

            for j in range(0, arr.shape[1]):

                pixelIntensity = arr[i][j]

                # if pixelIntensity == 0 and ignoreBackground:
                #     continue

                if j == arr.shape[1]-1:
                    glrlm[pixelIntensity][runLength] += 1
                else:
                    if arr[i][j] == arr[i][j+1]:
                        runLength += 1
                    else:
                        glrlm[pixelIntensity][runLength] += 1
                        runLength = 0

    # 90 Degrees. Compare Center Pixel to Below. Works 'down' columns.
    if angle == np.pi/2:

        for j in range(0, arr.shape[1]):

            runLength = 0

            for i in range(0, arr.shape[0]):

                pixelIntensity = arr[i][j]

                # if pixelIntensity == 0 and ignoreBackground:
                #     continue

                if i == arr.shape[0]-1:
                    glrlm[pixelIntensity][runLength] += 1
                else:
                    if arr[i][j] == arr[i+1][j]:
                        runLength += 1
                    else:
                        glrlm[pixelIntensity][runLength] += 1
                        runLength = 0

    elif angle == np.pi/4:  # 45 Degrees. Compare to pixels in the Above-Right and Below-Left

        for i in range(1, arr.shape[0]):

            runLength = 0

            for j in range(0, i+1):

                pixelIntensity = arr[i][j]

                # if pixelIntensity == 0 and ignoreBackground:
                #     continue

                if i == 0:
                    glrlm[pixelIntensity][runLength] += 1
                else:
                    if arr[i][j] == arr[i-1][j+1]:
                        runLength += 1
                        i -= 1
                    else:
                        glrlm[pixelIntensity][runLength] += 1
                        runLength = 0
                        i -= 1

        for j in range(1, arr.shape[1]-1):

            runLength = 0

            for i in range(arr.shape[0]-1, j-1, -1):

                pixelIntensity = arr[i][j]

                # if pixelIntensity == 0 and ignoreBackground:
                #     continue

                if j == arr.shape[1]-1:
                    glrlm[pixelIntensity][runLength] += 1
                else:
                    if arr[i][j] == arr[i-1][j+1]:
                        runLength += 1
                        j += 1
                        # continue
                    else:
                        glrlm[pixelIntensity][runLength] += 1
                        runLength = 0
                        j += 1

    # 135 Degrees. Compare to pixels in the Above-Left and Below-Right
    elif angle == np.pi*(135/180):

        for i in range(arr.shape[0]-2, -1, -1):

            runLength = 0

            for j in range(0, arr.shape[0]):

                pixelIntensity = arr[i][j]

                # if pixelIntensity == 0 and ignoreBackground:
                #     continue

                if i == arr.shape[0]-1:
                    glrlm[pixelIntensity][runLength] += 1
                    break
                else:
                    if arr[i][j] == arr[i+1][j+1]:
                        runLength += 1
                        i += 1
                    else:
                        glrlm[pixelIntensity][runLength] += 1
                        runLength = 0
                        i += 1

        for j in range(1, arr.shape[1]-1):

            runLength = 0

            for i in range(0, arr.shape[0]):

                pixelIntensity = arr[i][j]

                # if pixelIntensity == 0 and ignoreBackground:
                #     continue

                if j == arr.shape[1]-1:
                    glrlm[pixelIntensity][runLength] += 1
                    break
                else:
                    if arr[i][j] == arr[i+1][j+1]:
                        runLength += 1
                        j += 1
                    else:
                        glrlm[pixelIntensity][runLength] += 1
                        runLength = 0
                        j += 1

    return glrlm
