# -*- coding: utf-8 -*-
"""
@author: Joshua J.A. Poole

Constructs Gray-Level Cooccurance Matrix (GLCM) from image.

INPUT: Image in form of Numpy array.
OUTPIT: GLCM from image in form of Numpy array.

ARGUMENTS: 
    arr - Image in form of array.
    angle - Angle of calculation (0, 45, 90, or 135).
    bitDepth - Bitdepth of image. Determines size of GLCM.
"""
import numpy as np


def calc_glcm(arr, angle, bitDepth):

    glcm = np.zeros((2**bitDepth, 2**bitDepth))

    iRange = range(0, arr.shape[0])
    jRange = range(0, arr.shape[1])

    # Different angles require different comparisons.
    # Decides which path to take, depending on direction required.

    if angle == 0:  # 0 Degrees. Compare pixels to Left and Right.

        for i in iRange:

            for j in jRange:

                if j == 0:  # Left-Most Edge. Compare to right.
                    glcm[arr[i][j]][arr[i][j+1]] += 1
                elif j == arr.shape[1]-1:  # Right-Most Edge. Compare to left.
                    glcm[arr[i][j]][arr[i][j-1]] += 1
                else:  # All other pixels. Compare to both left and right.
                    glcm[arr[i][j]][arr[i][j+1]] += 1
                    glcm[arr[i][j]][arr[i][j-1]] += 1

    elif angle == np.pi/4:  # 45 Degrees. Compare to pixels in the Above-Right and Below-Left

        for i in iRange:

            for j in jRange:

                if i == 0 and j == 0:  # Topleft Corner. No comparison needed, as out of bounds.
                    continue
                # Bottom right corner. No comparison needed, as out of bounds.
                elif i == arr.shape[0]-1 and j == arr.shape[1]-1:
                    continue
                # Top and Right-Most Row and Column. Compare to Below-Left
                elif i == 0 or j == arr.shape[1]-1:
                    glcm[arr[i][j]][arr[i+1][j-1]] += 1
                # Bottom and Left-Most Row and Column. Compare to Above-Right.
                elif i == arr.shape[0]-1 or j == 0:
                    glcm[arr[i][j]][arr[i-1][j+1]] += 1
                # All other pixels. Compare to both Below-Left and Above-Right.
                else:
                    glcm[arr[i][j]][arr[i+1][j-1]] += 1
                    glcm[arr[i][j]][arr[i-1][j+1]] += 1

    elif angle == np.pi/2:  # 90 Degrees. Compare to Above and Below.

        for i in iRange:

            for j in jRange:

                if i == 0:  # Top Edge. Compare to Below.
                    glcm[arr[i][j]][arr[i+1][j]] += 1
                elif i == arr.shape[1]-1:  # Bottom Edge. Compare to Above.
                    glcm[arr[i][j]][arr[i-1][j]] += 1
                else:  # All other pixels. Compare to both Above and Below.
                    glcm[arr[i][j]][arr[i+1][j]] += 1
                    glcm[arr[i][j]][arr[i-1][j]] += 1

    # 135 Degrees. Compare to pixels in the Above-Left and Below-Right
    elif angle == np.pi*(135/180):

        for i in iRange:

            for j in jRange:

                # Top Right Corner. No comparison needed, as out of bounds.
                if i == 0 and j == arr.shape[1]-1:
                    continue
                # Bottom Leftcorner. No comparison needed, as out of bounds.
                elif i == arr.shape[0]-1 and j == 0:
                    continue
                elif i == 0 or j == 0:  # Top and Left-Most Row and Column. Compare to Below-Right
                    glcm[arr[i][j]][arr[i+1][j+1]] += 1
                # Bottom and Right-Most Row and Column. Compare to Above-Left.
                elif i == arr.shape[0]-1 or j == arr.shape[1]-1:
                    glcm[arr[i][j]][arr[i-1][j-1]] += 1
                # All other pixels. Compare to both Below-Right and Above-Left.
                else:
                    glcm[arr[i][j]][arr[i+1][j+1]] += 1
                    glcm[arr[i][j]][arr[i-1][j-1]] += 1

    return glcm
