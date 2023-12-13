# -*- coding: utf-8 -*-
"""
@author: Joshua J.A. Poole

Constructs Neighbouring Gray Tone Difference Matrix (NGTDM) from image.

INPUT: Image in form of Numpy array.
OUTPIT: NGTDM from image in form of Numpy array.

ARGUMENTS: 
    arr - Image in form of array.
    ignoreBackground - If true, ignores pixels with value 0. Prevents matrices from being too large. (Default = True)
    
"""
import numpy as np


def calc_ngtdm(arr, ignoreBackground):

    arr = arr.astype('i')

    maxIntensity = arr.max()
    totalSize = arr.shape[0]*arr.shape[1]

    ngtdm = np.zeros((maxIntensity + 1, 3))

    # Iterate through array

    for i in range(0, arr.shape[0]):

        for j in range(0, arr.shape[1]):

            pixelIntensity = arr[i][j]

            if pixelIntensity == 0 and ignoreBackground:
                continue

            # Check location of pixel for different comparisons:

            # Top left-most corner, compare to right, right-below, and below:
            if i == 0 and j == 0:

                # Find average value of neighbourhood

                neighbourhoodAverage = (
                    (1/3)*(arr[i][j+1]+arr[i+1][j+1] + arr[i+1][j])
                )

                # Calculate Neighbouring Graytone Difference

                neighbouringGrayDiff = abs(arr[i][j] - neighbourhoodAverage)

                # Increment number of intensity by one, and add neighbouringGrayDiff

                ngtdm[arr[i][j]][0] += 1

                ngtdm[arr[i][j]][2] += neighbouringGrayDiff

            # Top right-most corner, compare to left, left-below, and below:
            elif i == 0 and j == arr.shape[1]-1:

                # Find average value of neighbourhood

                neighbourhoodAverage = (
                    (1/3)*(arr[i][j-1]+arr[i+1][j-1] + arr[i+1][j])
                )

                # Calculate Neighbouring Graytone Difference

                neighbouringGrayDiff = abs(arr[i][j] - neighbourhoodAverage)

                # Increment number of intensity by one, and add neighbouringGrayDiff

                ngtdm[arr[i][j]][0] += 1

                ngtdm[arr[i][j]][2] += neighbouringGrayDiff

            #  Bottom left-most corner, compare to above, right above and right:
            elif i == arr.shape[0]-1 and j == 0:

                # Find average value of neighbourhood

                neighbourhoodAverage = (
                    (1/3)*(arr[i-1][j]+arr[i-1][j+1] + arr[i][j+1])
                )

                # Calculate Neighbouring Graytone Difference

                neighbouringGrayDiff = abs(arr[i][j] - neighbourhoodAverage)

                # Increment number of intensity by one, and add neighbouringGrayDiff

                ngtdm[arr[i][j]][0] += 1

                ngtdm[arr[i][j]][2] += neighbouringGrayDiff

            # Bottom right-most corner, compare to above, left above and left:
            elif i == arr.shape[0]-1 and j == arr.shape[1]-1:

                # Find average value of neighbourhood

                neighbourhoodAverage = (
                    (1/3)*(arr[i-1][j]+arr[i-1][j-1] + arr[i][j-1])
                )

                # Calculate Neighbouring Graytone Difference

                neighbouringGrayDiff = abs(arr[i][j] - neighbourhoodAverage)

                # Increment number of intensity by one, and add neighbouringGrayDiff

                ngtdm[arr[i][j]][0] += 1

                ngtdm[arr[i][j]][2] += neighbouringGrayDiff

            # Top row (Non-corner), compare to left, left-below, below, right-below and right:
            elif i == 0:

                # Find average value of neighbourhood

                neighbourhoodAverage = (
                    (1/5)*(arr[i][j-1]+arr[i+1][j-1]
                           + arr[i+1][j]+arr[i+1][j+1]
                           + arr[i][j+1])
                )

                # Calculate Neighbouring Graytone Difference

                neighbouringGrayDiff = abs(arr[i][j] - neighbourhoodAverage)

                # Increment number of intensity by one, and add neighbouringGrayDiff

                ngtdm[arr[i][j]][0] += 1

                ngtdm[arr[i][j]][2] += neighbouringGrayDiff

            # Bottom row (non corner), compare to left, left-above, above, right-above and right:
            elif i == arr.shape[0]-1:

                # Find average value of neighbourhood

                neighbourhoodAverage = (1/5)*(arr[i][j-1]+arr[i-1][j-1]
                                              + arr[i-1][j]+arr[i-1][j+1]
                                              + arr[i][j+1])

                # Calculate Neighbouring Graytone Difference

                neighbouringGrayDiff = abs(arr[i][j] - neighbourhoodAverage)

                # Increment number of intensity by one, and add neighbouringGrayDiff

                ngtdm[arr[i][j]][0] += 1

                ngtdm[arr[i][j]][2] += neighbouringGrayDiff

            # Left-most Edge (non-corner), compare to above, right-above, right, right-below, and below:
            elif j == 0:

                # Find average value of neighbourhood

                neighbourhoodAverage = (1/5)*(arr[i-1][j]+arr[i-1][j+1]
                                              + arr[i][j+1]+arr[i+1][j+1]
                                              + arr[i+1][j])

                # Calculate Neighbouring Graytone Difference

                neighbouringGrayDiff = abs(arr[i][j] - neighbourhoodAverage)

                # Increment number of intensity by one, and add neighbouringGrayDiff

                ngtdm[arr[i][j]][0] += 1

                ngtdm[arr[i][j]][2] += neighbouringGrayDiff

            # Right-most Edge (non-corner), compare to above, left-above, left, left-below, and below:
            elif j == arr.shape[1]-1:

                # Find average value of neighbourhood

                neighbourhoodAverage = (
                    (1/5)*(arr[i-1][j]+arr[i-1][j-1] +
                           arr[i][j-1]+arr[i+1][j-1] +
                           arr[i+1][j])
                )

                # Calculate Neighbouring Graytone Difference

                neighbouringGrayDiff = abs(arr[i][j] - neighbourhoodAverage)

                # Increment number of intensity by one, and add neighbouringGrayDiff

                ngtdm[arr[i][j]][0] += 1

                ngtdm[arr[i][j]][2] += neighbouringGrayDiff

            # Non-edge pixel. Compare to all pixel in neighbourhood.
            else:

                # Find average value of neighbourhood

                neighbourhoodAverage = (
                    (1/8)*(arr[i-1][j-1]+arr[i-1][j] +
                           arr[i-1][j+1]+arr[i][j-1] +
                           arr[i][j+1]+arr[i+1][j-1] +
                           arr[i+1][j]+arr[i+1][j+1])
                )

                # Calculate Neighbouring Graytone Difference

                neighbouringGrayDiff = abs(arr[i][j] - neighbourhoodAverage)

                # Increment number of intensity by one, and add neighbouringGrayDiff

                ngtdm[arr[i][j]][0] += 1

                ngtdm[arr[i][j]][2] += neighbouringGrayDiff

    for i in range(0, ngtdm.shape[0]):

        ngtdm[i][1] = ngtdm[i][0]/totalSize

    return ngtdm


arr = np.array([[0, 1, 1, 2, 0],
                [0, 1, 2, 1, 1],
                [0, 0, 2, 1, 0],
                [0, 2, 3, 2, 1],
                [2, 3, 2, 3, 0]])

gldm = calc_ngtdm(arr, ignoreBackground=False)
