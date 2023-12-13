# -*- coding: utf-8 -*-
"""
@author: Joshua J.A. Poole

Constructs Gray-Level Dependence Matrix (GLDM) from image.

INPUT: Image in form of Numpy array.
OUTPIT: GLDM from image in form of Numpy array.

ARGUMENTS: 
    arr - Image in form of array.
    alpha - Distance from center pixel for comparison.
    bitDepth - Bitdepth of image. Determines size of GLDM.
"""

import numpy as np


def calc_gldm(arr, alpha, bitDepth):

    arr = arr.astype('i')

    numIntensities = 2**bitDepth
    gldm = np.zeros((numIntensities, 9))

    iRange = range(0, arr.shape[0])
    jRange = range(0, arr.shape[1])

    for i in iRange:

        for j in jRange:

            pixelIntensity = arr[i][j]
            dependentPixels = 0

            # Check location of pixel for different comparisons:

            # Top left-most corner, compare to right, right-below, and below:
            if i == 0 and j == 0:

                # Calculate how many dependent pixels.

                if abs(arr[i][j]-arr[i][j+1]) <= alpha:  # Right
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i+1][j+1]) <= alpha:  # Right-Below
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i+1][j]) <= alpha:  # Below
                    dependentPixels += 1

            # Top right-most corner, compare to left, left-below, and below:
            elif i == 0 and j == arr.shape[1]-1:

                # Calculate how many dependent pixels.

                if abs(arr[i][j]-arr[i][j-1]) <= alpha:  # Left
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i+1][j-1]) <= alpha:  # Left-Below
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i+1][j]) <= alpha:  # Below
                    dependentPixels += 1

            #  Bottom left-most corner, compare to above, right above and right:
            elif i == arr.shape[0]-1 and j == 0:

                # Calculate how many dependent pixels.

                if abs(arr[i][j]-arr[i-1][j]) <= alpha:  # Above
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i-1][j+1]) <= alpha:  # Right-Above
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i][j+1]) <= alpha:  # Right
                    dependentPixels += 1

            # Bottom right-most corner, compare to above, left above and left:
            elif i == arr.shape[0]-1 and j == arr.shape[1]-1:

                # Calculate how many dependent pixels.

                if abs(arr[i][j]-arr[i-1][j]) <= alpha:  # Above
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i-1][j-1]) <= alpha:  # Above-Left
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i][j-1]) <= alpha:  # Left
                    dependentPixels += 1

            # Top row (Non-corner), compare to left, left-below, below, right-below and right:
            elif i == 0:

                # Calculate how many dependent pixels.

                if abs(arr[i][j]-arr[i][j-1]) <= alpha:  # Left
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i+1][j-1]) <= alpha:  # Left-Below
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i+1][j]) <= alpha:  # Below
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i-1][j+1]) <= alpha:  # Right-Above
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i][j+1]) <= alpha:  # Right
                    dependentPixels += 1

            # Bottom row (non corner), compare to left, left-above, above, right-above and right:
            elif i == arr.shape[0]-1:

                # Calculate how many dependent pixels.

                if abs(arr[i][j]-arr[i][j-1]) <= alpha:  # Left
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i-1][j-1]) <= alpha:  # Above-Left
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i-1][j]) <= alpha:  # Above
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i-1][j+1]) <= alpha:  # Right-Above
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i][j+1]) <= alpha:  # Right
                    dependentPixels += 1

            # Left-most Edge (non-corner), compare to above, right-above, right, right-below, and below:
            elif j == 0:

                # Calculate how many dependent pixels.

                if abs(arr[i][j]-arr[i-1][j]) <= alpha:  # Above
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i-1][j+1]) <= alpha:  # Right-Above
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i][j+1]) <= alpha:  # Right
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i+1][j+1]) <= alpha:  # Right-Below
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i+1][j]) <= alpha:  # Below
                    dependentPixels += 1

            # Right-most Edge (non-corner), compare to above, left-above, left, left-below, and below:
            elif j == arr.shape[1]-1:

                # Calculate how many dependent pixels.

                if abs(arr[i][j]-arr[i-1][j]) <= alpha:  # Above
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i-1][j-1]) <= alpha:  # Above-Left
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i][j-1]) <= alpha:  # Left
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i+1][j-1]) <= alpha:  # Left-Below
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i+1][j]) <= alpha:  # Below
                    dependentPixels += 1

            # Non-edge pixel. Compare to all pixel in neighbourhood.
            else:

                if abs(arr[i][j]-arr[i][j-1]) <= alpha:  # Left
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i-1][j-1]) <= alpha:  # Above-Left
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i-1][j]) <= alpha:  # Above
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i-1][j+1]) <= alpha:  # Right-Above
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i][j+1]) <= alpha:  # Right
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i+1][j+1]) <= alpha:  # Right-Below
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i+1][j]) <= alpha:  # Below
                    dependentPixels += 1
                if abs(arr[i][j]-arr[i+1][j-1]) <= alpha:  # Left-Below
                    dependentPixels += 1

            # if gldm.shape[1] < dependentPixels + 1:
            #     for colNum in range(1, dependentPixels - gldm.shape[1] + 2):
            #         gldm = np.column_stack((gldm, np.zeros(gldm.shape[0])))

            gldm[pixelIntensity][dependentPixels] += 1

    return gldm
