# -*- coding: utf-8 -*-
"""
@author: Joshua J.A. Poole

Constructs Gray-Level Size Zone Matrix (GLSZM) from image.

INPUT: Image in form of Numpy array.
OUTPIT: GLSZM from image in form of Numpy array.

ARGUMENTS: 
    arr - Image in form of array.
    bitDepth - Bitdepth of image. Determines size of GLDM.
    ignoreBackground - If true, ignores pixels with value 0. Prevents matrices from being too large. (Default = True)
"""

#!/usr/bin/env python

from collections import deque
import numpy as np


def calc_glszm(array, bitDepth, ignoreBackground):

    arr = array.astype('h')
    coordQueue = deque()
    # glszm = np.zeros((2**bitDepth,1))

    iRange = range(0, arr.shape[0])
    jRange = range(0, arr.shape[1])

    maxRegionSize = 1

    # Iterate through array

    for i in iRange:

        for j in jRange:

            # Record Pixel Intensity for comparison.
            pixelIntensity = arr[i][j]
            regionSize = 1

            if pixelIntensity == 0 and ignoreBackground == True:
                arr[i][j] = -1

            if arr[i][j] != -1:

                # Check location of pixel for different comparisons:

                # Top left-most corner, compare to right, right-below, and below:
                if i == 0 and j == 0:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.

                    if arr[i][j+1] == pixelIntensity:  # Right
                        coordQueue.append((i, j+1))
                        arr[i][j+1] = -1
                    if arr[i+1][j+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((i+1, j+1))
                        arr[i+1][j+1] = -1
                    if arr[i+1][j] == pixelIntensity:  # Below
                        coordQueue.append((i+1, j))
                        arr[i+1][j] = -1

                # Top right-most corner, compare to left, left-below, and below:
                elif i == 0 and j == arr.shape[1]-1:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.

                    if arr[i][j-1] == pixelIntensity:  # Left
                        coordQueue.append((i, j-1))
                        arr[i][j-1] = -1
                    if arr[i+1][j-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((i+1, j-1))
                        arr[i+1][j-1] = -1
                    if arr[i+1][j] == pixelIntensity:  # Below
                        coordQueue.append((i+1, j))
                        arr[i+1][j] = -1

                #  Bottom left-most corner, compare to above, right above and right:
                elif i == arr.shape[0]-1 and j == 0:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.
                    if arr[i-1][j] == pixelIntensity:  # Above
                        coordQueue.append((i-1, j))
                        arr[i-1][j] = -1
                    if arr[i-1][j+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((i-1, j+1))
                        arr[i-1][j+1] = -1
                    if arr[i][j+1] == pixelIntensity:  # Right
                        coordQueue.append((i, j+1))
                        arr[i][j+1] = -1

                # Bottom right-most corner, compare to above, left above and left:
                elif i == arr.shape[0]-1 and j == arr.shape[1]-1:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.
                    if arr[i-1][j] == pixelIntensity:  # Above
                        coordQueue.append((i-1, j))
                        arr[i-1][j] = -1
                    if arr[i-1][j-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((i-1, j-1))
                        arr[i-1][j-1] = -1
                    if arr[i][j-1] == pixelIntensity:  # Left
                        coordQueue.append((i, j-1))
                        arr[i][j-1] = -1

                # Top row (Non-corner), compare to left, left-below, below, right-below and right:
                elif i == 0:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.

                    if arr[i][j-1] == pixelIntensity:  # Left
                        coordQueue.append((i, j-1))
                        arr[i][j-1] = -1
                    if arr[i+1][j-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((i+1, j-1))
                        arr[i+1][j-1] = -1
                    if arr[i+1][j] == pixelIntensity:  # Below
                        coordQueue.append((i+1, j))
                        arr[i+1][j] = -1
                    if arr[i+1][j+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((i+1, j+1))
                        arr[i+1][j+1] = -1
                    if arr[i][j+1] == pixelIntensity:  # Right
                        coordQueue.append((i, j+1))
                        arr[i][j+1] = -1

                # Bottom row (non corner), compare to left, left-above, above, right-above and right:
                elif i == arr.shape[0]-1:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.
                    if arr[i][j-1] == pixelIntensity:  # Left
                        coordQueue.append((i, j-1))
                        arr[i][j-1] = -1
                    if arr[i-1][j-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((i-1, j-1))
                        arr[i-1][j-1] = -1
                    if arr[i-1][j] == pixelIntensity:  # Above
                        coordQueue.append((i-1, j))
                        arr[i-1][j] = -1
                    if arr[i-1][j+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((i-1, j+1))
                        arr[i-1][j+1] = -1
                    if arr[i][j+1] == pixelIntensity:  # Right
                        coordQueue.append((i, j+1))
                        arr[i][j+1] = -1

                # Left-most Edge (non-corner), compare to above, right-above, right, right-below, and below:
                elif j == 0:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i, j] = -1

                    # Store pixel coords in queue if they match.
                    if arr[i-1][j] == pixelIntensity:  # Above
                        coordQueue.append((i-1, j))
                        arr[i-1][j] = -1
                    if arr[i-1][j+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((i-1, j+1))
                        arr[i-1][j+1] = -1
                    if arr[i][j+1] == pixelIntensity:  # Right
                        coordQueue.append((i, j+1))
                        arr[i][j+1] = -1
                    if arr[i+1][j+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((i+1, j+1))
                        arr[i+1][j+1] = -1
                    if arr[i+1][j] == pixelIntensity:  # Below
                        coordQueue.append((i+1, j))
                        arr[i+1][j] = -1

                # Right-most Edge (non-corner), compare to above, left-above, left, left-below, and below:
                elif j == arr.shape[1]-1:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.
                    if arr[i-1][j] == pixelIntensity:  # Above
                        coordQueue.append((i-1, j))
                        arr[i-1][j] = -1
                    if arr[i-1][j-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((i-1, j-1))
                        arr[i-1][j-1] = -1
                    if arr[i][j-1] == pixelIntensity:  # Left
                        coordQueue.append((i, j-1))
                        arr[i][j-1] = -1
                    if arr[i+1][j-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((i+1, j-1))
                        arr[i+1][j-1] = -1
                    if arr[i+1][j] == pixelIntensity:  # Below
                        coordQueue.append((i+1, j))
                        arr[i+1][j] = -1

                # Non-edge pixel. Compare to all pixel in neighbourhood.
                else:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.
                    if arr[i][j-1] == pixelIntensity:  # Left
                        coordQueue.append((i, j-1))
                        arr[i][j-1] = -1
                    if arr[i-1][j-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((i-1, j-1))
                        arr[i-1][j-1] = -1
                    if arr[i-1][j] == pixelIntensity:  # Above
                        coordQueue.append((i-1, j))
                        arr[i-1][j] = -1
                    if arr[i-1][j+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((i-1, j+1))
                        arr[i-1][j+1] = -1
                    if arr[i][j+1] == pixelIntensity:  # Right
                        coordQueue.append((i, j+1))
                        arr[i][j+1] = -1
                    if arr[i+1][j+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((i+1, j+1))
                        arr[i+1][j+1] = -1
                    if arr[i+1][j] == pixelIntensity:  # Below
                        coordQueue.append((i+1, j))
                        arr[i+1][j] = -1
                    if arr[i+1][j-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((i+1, j-1))
                        arr[i+1][j-1] = -1

            # Check coords stored in queue.

            while coordQueue:

                # Remove coord from queue, increment region size

                coord = coordQueue.popleft()
                regionSize += 1

                # Check location of pixel for different comparisons:

                # Top-leftmost corner, compare to right, right-below, and below:
                if (coord[0] == 0) and (coord[1] == 0):

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]][coord[1]+1] == pixelIntensity:  # Right
                        coordQueue.append((coord[0], coord[1]+1))
                        arr[coord[0]][coord[1]+1] = -1

                    if arr[coord[0]+1][coord[1]+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((coord[0]+1, coord[1]+1))
                        arr[coord[0]+1][coord[1]+1] = -1

                    if arr[coord[0]+1][coord[1]] == pixelIntensity:  # Below
                        coordQueue.append((coord[0]+1, coord[1]))
                        arr[coord[0]+1][coord[1]] = -1

                # Top-rightmost corner, compare to left, left-below, and below:
                elif (coord[0] == 0) and (coord[1] == arr.shape[1]-1):

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]][coord[1]-1] == pixelIntensity:  # Left
                        coordQueue.append((coord[0], coord[1]-1))
                        arr[coord[0]][coord[1]-1] = -1

                    if arr[coord[0]+1][coord[1]-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((coord[0]+1, coord[1]-1))
                        arr[coord[0]+1][coord[1]-1] = -1

                    if arr[coord[0]+1][coord[1]] == pixelIntensity:  # Below
                        coordQueue.append((coord[0]+1, coord[1]))
                        arr[coord[0]+1][coord[1]] = -1

                # Bottom left-most corner, compare to above, right above and right:
                elif (coord[0] == arr.shape[0]-1) and (coord[1] == 0):

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]-1][coord[1]] == pixelIntensity:  # Above
                        coordQueue.append((coord[0]-1, coord[1]))
                        arr[coord[0]-1][coord[1]] = -1

                    if arr[coord[0]-1][coord[1]+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((coord[0]-1, coord[1]+1))
                        arr[coord[0]-1][coord[1]+1] = -1

                    if arr[coord[0]][coord[1]+1] == pixelIntensity:  # Right
                        coordQueue.append((coord[0], coord[1]+1))
                        arr[coord[0]][coord[1]+1] = -1

                # Bottom right-most corner, compare to above, left above and left:
                elif (coord[0] == arr.shape[0]-1) and (coord[1] == arr.shape[1]-1):

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]-1][coord[1]] == pixelIntensity:  # Above
                        coordQueue.append((coord[0]-1, coord[1]))
                        arr[coord[0]-1][coord[1]] = -1

                    if arr[coord[0]-1][coord[1]-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((coord[0]-1, coord[1]-1))
                        arr[coord[0]-1][coord[1]-1] = -1

                    if arr[coord[0]][coord[1]-1] == pixelIntensity:  # Left
                        coordQueue.append((coord[0], coord[1]-1))
                        arr[coord[0]][coord[1]-1] = -1

                # Top row (Non-corner), compare to left, left-below, below, right-below and right:
                elif coord[0] == 0:

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]][coord[1]-1] == pixelIntensity:  # Left
                        coordQueue.append((coord[0], coord[1]-1))
                        arr[coord[0]][coord[1]-1] = -1

                    if arr[coord[0]+1][coord[1]-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((coord[0]+1, coord[1]-1))
                        arr[coord[0]+1][coord[1]-1] = -1

                    if arr[coord[0]+1][coord[1]] == pixelIntensity:  # Below
                        coordQueue.append((coord[0]+1, coord[1]))
                        arr[coord[0]+1][coord[1]] = -1

                    if arr[coord[0]+1][coord[1]+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((coord[0]+1, coord[1]+1))
                        arr[coord[0]+1][coord[1]+1] = -1

                    if arr[coord[0]][coord[1]+1] == pixelIntensity:  # Right
                        coordQueue.append((coord[0], coord[1]+1))
                        arr[coord[0]][coord[1]+1] = -1

                # Bottom row (non corner), compare to left, left-above, above, right-above and right:
                elif coord[0] == arr.shape[0]-1:

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]][coord[1]-1] == pixelIntensity:  # Left
                        coordQueue.append((coord[0], coord[1]-1))
                        arr[coord[0]][coord[1]-1] = -1

                    if arr[coord[0]-1][coord[1]-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((coord[0]-1, coord[1]-1))
                        arr[coord[0]-1][coord[1]-1] = -1

                    if arr[coord[0]-1][coord[1]] == pixelIntensity:  # Above
                        coordQueue.append((coord[0]-1, coord[1]))
                        arr[coord[0]-1][coord[1]] = -1

                    if arr[coord[0]-1][coord[1]+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((coord[0]-1, coord[1]+1))
                        arr[coord[0]-1][coord[1]+1] = -1

                    if arr[coord[0]][coord[1]+1] == pixelIntensity:  # Right
                        coordQueue.append((coord[0], coord[1]+1))
                        arr[coord[0]][coord[1]+1] = -1

                # Left-most Edge (non-corner), compare to above, right-above, right, right-below, and below:
                elif coord[1] == 0:

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]-1][coord[1]] == pixelIntensity:  # Above
                        coordQueue.append((coord[0]-1, coord[1]))
                        arr[coord[0]-1][coord[1]] = -1

                    if arr[coord[0]-1][coord[1]+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((coord[0]-1, coord[1]+1))
                        arr[coord[0]-1][coord[1]+1] = -1

                    if arr[coord[0]][coord[1]+1] == pixelIntensity:  # Right
                        coordQueue.append((coord[0], coord[1]+1))
                        arr[coord[0]][coord[1]+1] = -1

                    if arr[coord[0]+1][coord[1]+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((coord[0]+1, coord[1]+1))
                        arr[coord[0]+1][coord[1]+1] = -1

                    if arr[coord[0]+1][coord[1]] == pixelIntensity:  # Below
                        coordQueue.append((coord[0]+1, coord[1]))
                        arr[coord[0]+1][coord[1]] = -1

                # Right-most Edge (non-corner), compare to above, left-above, left, left-below, and below:
                elif coord[1] == arr.shape[1]-1:

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]-1][coord[1]] == pixelIntensity:  # Above
                        coordQueue.append((coord[0]-1, coord[1]))
                        arr[coord[0]-1][coord[1]] = -1

                    if arr[coord[0]-1][coord[1]-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((coord[0]-1, coord[1]-1))
                        arr[coord[0]-1][coord[1]-1] = -1

                    if arr[coord[0]][coord[1]-1] == pixelIntensity:  # Left
                        coordQueue.append((coord[0], coord[1]-1))
                        arr[coord[0]][coord[1]-1] = -1

                    if arr[coord[0]+1][coord[1]-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((coord[0]+1, coord[1]-1))
                        arr[coord[0]+1][coord[1]-1] = -1

                    if arr[coord[0]+1][coord[1]] == pixelIntensity:  # Below
                        coordQueue.append((coord[0]+1, coord[1]))
                        arr[coord[0]+1][coord[1]] = -1

                # Non-edge pixel. Compare to all pixel in neighbourhood.
                else:

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]][coord[1]-1] == pixelIntensity:  # Left
                        coordQueue.append((coord[0], coord[1]-1))
                        arr[coord[0]][coord[1]-1] = -1

                    if arr[coord[0]-1][coord[1]-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((coord[0]-1, coord[1]-1))
                        arr[coord[0]-1][coord[1]-1] = -1

                    if arr[coord[0]-1][coord[1]] == pixelIntensity:  # Above
                        coordQueue.append((coord[0]-1, coord[1]))
                        arr[coord[0]-1][coord[1]] = -1

                    if arr[coord[0]-1][coord[1]+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((coord[0]-1, coord[1]+1))
                        arr[coord[0]-1][coord[1]+1] = -1

                    if arr[coord[0]][coord[1]+1] == pixelIntensity:  # Right
                        coordQueue.append((coord[0], coord[1]+1))
                        arr[coord[0]][coord[1]+1] = -1

                    if arr[coord[0]+1][coord[1]+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((coord[0]+1, coord[1]+1))
                        arr[coord[0]+1][coord[1]+1] = -1

                    if arr[coord[0]+1][coord[1]] == pixelIntensity:  # Below
                        coordQueue.append((coord[0]+1, coord[1]))
                        arr[coord[0]+1][coord[1]] = -1

                    if arr[coord[0]+1][coord[1]-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((coord[0]+1, coord[1]-1))
                        arr[coord[0]+1][coord[1]-1] = -1

            if regionSize > maxRegionSize:
                maxRegionSize = regionSize

    glszm = np.zeros((2**bitDepth, maxRegionSize))
    arr = array.astype('h')

    # del coord

    # Iterate through array

    for i in iRange:

        for j in jRange:

            # Record Pixel Intensity for comparison.
            pixelIntensity = arr[i][j]
            regionSize = 0

            if pixelIntensity == 0 and ignoreBackground == True:
                arr[i][j] = -1

            if arr[i][j] != -1:

                # Check location of pixel for different comparisons:

                # Top left-most corner, compare to right, right-below, and below:
                if i == 0 and j == 0:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.

                    if arr[i][j+1] == pixelIntensity:  # Right
                        coordQueue.append((i, j+1))
                        arr[i][j+1] = -1
                    if arr[i+1][j+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((i+1, j+1))
                        arr[i+1][j+1] = -1
                    if arr[i+1][j] == pixelIntensity:  # Below
                        coordQueue.append((i+1, j))
                        arr[i+1][j] = -1

                # Top right-most corner, compare to left, left-below, and below:
                elif i == 0 and j == arr.shape[1]-1:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.

                    if arr[i][j-1] == pixelIntensity:  # Left
                        coordQueue.append((i, j-1))
                        arr[i][j-1] = -1
                    if arr[i+1][j-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((i+1, j-1))
                        arr[i+1][j-1] = -1
                    if arr[i+1][j] == pixelIntensity:  # Below
                        coordQueue.append((i+1, j))
                        arr[i+1][j] = -1

                #  Bottom left-most corner, compare to above, right above and right:
                elif i == arr.shape[0]-1 and j == 0:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.
                    if arr[i-1][j] == pixelIntensity:  # Above
                        coordQueue.append((i-1, j))
                        arr[i-1][j] = -1
                    if arr[i-1][j+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((i-1, j+1))
                        arr[i-1][j+1] = -1
                    if arr[i][j+1] == pixelIntensity:  # Right
                        coordQueue.append((i, j+1))
                        arr[i][j+1] = -1

                # Bottom right-most corner, compare to above, left above and left:
                elif i == arr.shape[0]-1 and j == arr.shape[1]-1:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.
                    if arr[i-1][j] == pixelIntensity:  # Above
                        coordQueue.append((i-1, j))
                        arr[i-1][j] = -1
                    if arr[i-1][j-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((i-1, j-1))
                        arr[i-1][j-1] = -1
                    if arr[i][j-1] == pixelIntensity:  # Left
                        coordQueue.append((i, j-1))
                        arr[i][j-1] = -1

                # Top row (Non-corner), compare to left, left-below, below, right-below and right:
                elif i == 0:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.

                    if arr[i][j-1] == pixelIntensity:  # Left
                        coordQueue.append((i, j-1))
                        arr[i][j-1] = -1
                    if arr[i+1][j-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((i+1, j-1))
                        arr[i+1][j-1] = -1
                    if arr[i+1][j] == pixelIntensity:  # Below
                        coordQueue.append((i+1, j))
                        arr[i+1][j] = -1
                    if arr[i+1][j+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((i+1, j+1))
                        arr[i+1][j+1] = -1
                    if arr[i][j+1] == pixelIntensity:  # Right
                        coordQueue.append((i, j+1))
                        arr[i][j+1] = -1

                # Bottom row (non corner), compare to left, left-above, above, right-above and right:
                elif i == arr.shape[0]-1:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.
                    if arr[i][j-1] == pixelIntensity:  # Left
                        coordQueue.append((i, j-1))
                        arr[i][j-1] = -1
                    if arr[i-1][j-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((i-1, j-1))
                        arr[i-1][j-1] = -1
                    if arr[i-1][j] == pixelIntensity:  # Above
                        coordQueue.append((i-1, j))
                        arr[i-1][j] = -1
                    if arr[i-1][j+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((i-1, j+1))
                        arr[i-1][j+1] = -1
                    if arr[i][j+1] == pixelIntensity:  # Right
                        coordQueue.append((i, j+1))
                        arr[i][j+1] = -1

                # Left-most Edge (non-corner), compare to above, right-above, right, right-below, and below:
                elif j == 0:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i, j] = -1

                    # Store pixel coords in queue if they match.
                    if arr[i-1][j] == pixelIntensity:  # Above
                        coordQueue.append((i-1, j))
                        arr[i-1][j] = -1
                    if arr[i-1][j+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((i-1, j+1))
                        arr[i-1][j+1] = -1
                    if arr[i][j+1] == pixelIntensity:  # Right
                        coordQueue.append((i, j+1))
                        arr[i][j+1] = -1
                    if arr[i+1][j+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((i+1, j+1))
                        arr[i+1][j+1] = -1
                    if arr[i+1][j] == pixelIntensity:  # Below
                        coordQueue.append((i+1, j))
                        arr[i+1][j] = -1

                # Right-most Edge (non-corner), compare to above, left-above, left, left-below, and below:
                elif j == arr.shape[1]-1:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.
                    if arr[i-1][j] == pixelIntensity:  # Above
                        coordQueue.append((i-1, j))
                        arr[i-1][j] = -1
                    if arr[i-1][j-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((i-1, j-1))
                        arr[i-1][j-1] = -1
                    if arr[i][j-1] == pixelIntensity:  # Left
                        coordQueue.append((i, j-1))
                        arr[i][j-1] = -1
                    if arr[i+1][j-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((i+1, j-1))
                        arr[i+1][j-1] = -1
                    if arr[i+1][j] == pixelIntensity:  # Below
                        coordQueue.append((i+1, j))
                        arr[i+1][j] = -1

                # Non-edge pixel. Compare to all pixel in neighbourhood.
                else:

                    # Set pixel value to -1 to avoid checking again.

                    arr[i][j] = -1

                    # Store pixel coords in queue if they match.
                    if arr[i][j-1] == pixelIntensity:  # Left
                        coordQueue.append((i, j-1))
                        arr[i][j-1] = -1
                    if arr[i-1][j-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((i-1, j-1))
                        arr[i-1][j-1] = -1
                    if arr[i-1][j] == pixelIntensity:  # Above
                        coordQueue.append((i-1, j))
                        arr[i-1][j] = -1
                    if arr[i-1][j+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((i-1, j+1))
                        arr[i-1][j+1] = -1
                    if arr[i][j+1] == pixelIntensity:  # Right
                        coordQueue.append((i, j+1))
                        arr[i][j+1] = -1
                    if arr[i+1][j+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((i+1, j+1))
                        arr[i+1][j+1] = -1
                    if arr[i+1][j] == pixelIntensity:  # Below
                        coordQueue.append((i+1, j))
                        arr[i+1][j] = -1
                    if arr[i+1][j-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((i+1, j-1))
                        arr[i+1][j-1] = -1

            # Check coords stored in queue.

            while coordQueue:

                # Remove coord from queue, increment region size

                coord = coordQueue.popleft()
                regionSize += 1

                # Check location of pixel for different comparisons:

                # Top-leftmost corner, compare to right, right-below, and below:
                if (coord[0] == 0) and (coord[1] == 0):

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]][coord[1]+1] == pixelIntensity:  # Right
                        coordQueue.append((coord[0], coord[1]+1))
                        arr[coord[0]][coord[1]+1] = -1

                    if arr[coord[0]+1][coord[1]+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((coord[0]+1, coord[1]+1))
                        arr[coord[0]+1][coord[1]+1] = -1

                    if arr[coord[0]+1][coord[1]] == pixelIntensity:  # Below
                        coordQueue.append((coord[0]+1, coord[1]))
                        arr[coord[0]+1][coord[1]] = -1

                # Top-rightmost corner, compare to left, left-below, and below:
                elif (coord[0] == 0) and (coord[1] == arr.shape[1]-1):

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]][coord[1]-1] == pixelIntensity:  # Left
                        coordQueue.append((coord[0], coord[1]-1))
                        arr[coord[0]][coord[1]-1] = -1

                    if arr[coord[0]+1][coord[1]-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((coord[0]+1, coord[1]-1))
                        arr[coord[0]+1][coord[1]-1] = -1

                    if arr[coord[0]+1][coord[1]] == pixelIntensity:  # Below
                        coordQueue.append((coord[0]+1, coord[1]))
                        arr[coord[0]+1][coord[1]] = -1

                # Bottom left-most corner, compare to above, right above and right:
                elif (coord[0] == arr.shape[0]-1) and (coord[1] == 0):

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]-1][coord[1]] == pixelIntensity:  # Above
                        coordQueue.append((coord[0]-1, coord[1]))
                        arr[coord[0]-1][coord[1]] = -1

                    if arr[coord[0]-1][coord[1]+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((coord[0]-1, coord[1]+1))
                        arr[coord[0]-1][coord[1]+1] = -1

                    if arr[coord[0]][coord[1]+1] == pixelIntensity:  # Right
                        coordQueue.append((coord[0], coord[1]+1))
                        arr[coord[0]][coord[1]+1] = -1

                # Bottom right-most corner, compare to above, left above and left:
                elif (coord[0] == arr.shape[0]-1) and (coord[1] == arr.shape[1]-1):

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]-1][coord[1]] == pixelIntensity:  # Above
                        coordQueue.append((coord[0]-1, coord[1]))
                        arr[coord[0]-1][coord[1]] = -1

                    if arr[coord[0]-1][coord[1]-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((coord[0]-1, coord[1]-1))
                        arr[coord[0]-1][coord[1]-1] = -1

                    if arr[coord[0]][coord[1]-1] == pixelIntensity:  # Left
                        coordQueue.append((coord[0], coord[1]-1))
                        arr[coord[0]][coord[1]-1] = -1

                # Top row (Non-corner), compare to left, left-below, below, right-below and right:
                elif coord[0] == 0:

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]][coord[1]-1] == pixelIntensity:  # Left
                        coordQueue.append((coord[0], coord[1]-1))
                        arr[coord[0]][coord[1]-1] = -1

                    if arr[coord[0]+1][coord[1]-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((coord[0]+1, coord[1]-1))
                        arr[coord[0]+1][coord[1]-1] = -1

                    if arr[coord[0]+1][coord[1]] == pixelIntensity:  # Below
                        coordQueue.append((coord[0]+1, coord[1]))
                        arr[coord[0]+1][coord[1]] = -1

                    if arr[coord[0]+1][coord[1]+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((coord[0]+1, coord[1]+1))
                        arr[coord[0]+1][coord[1]+1] = -1

                    if arr[coord[0]][coord[1]+1] == pixelIntensity:  # Right
                        coordQueue.append((coord[0], coord[1]+1))
                        arr[coord[0]][coord[1]+1] = -1

                # Bottom row (non corner), compare to left, left-above, above, right-above and right:
                elif coord[0] == arr.shape[0]-1:

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]][coord[1]-1] == pixelIntensity:  # Left
                        coordQueue.append((coord[0], coord[1]-1))
                        arr[coord[0]][coord[1]-1] = -1

                    if arr[coord[0]-1][coord[1]-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((coord[0]-1, coord[1]-1))
                        arr[coord[0]-1][coord[1]-1] = -1

                    if arr[coord[0]-1][coord[1]] == pixelIntensity:  # Above
                        coordQueue.append((coord[0]-1, coord[1]))
                        arr[coord[0]-1][coord[1]] = -1

                    if arr[coord[0]-1][coord[1]+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((coord[0]-1, coord[1]+1))
                        arr[coord[0]-1][coord[1]+1] = -1

                    if arr[coord[0]][coord[1]+1] == pixelIntensity:  # Right
                        coordQueue.append((coord[0], coord[1]+1))
                        arr[coord[0]][coord[1]+1] = -1

                # Left-most Edge (non-corner), compare to above, right-above, right, right-below, and below:
                elif coord[1] == 0:

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]-1][coord[1]] == pixelIntensity:  # Above
                        coordQueue.append((coord[0]-1, coord[1]))
                        arr[coord[0]-1][coord[1]] = -1

                    if arr[coord[0]-1][coord[1]+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((coord[0]-1, coord[1]+1))
                        arr[coord[0]-1][coord[1]+1] = -1

                    if arr[coord[0]][coord[1]+1] == pixelIntensity:  # Right
                        coordQueue.append((coord[0], coord[1]+1))
                        arr[coord[0]][coord[1]+1] = -1

                    if arr[coord[0]+1][coord[1]+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((coord[0]+1, coord[1]+1))
                        arr[coord[0]+1][coord[1]+1] = -1

                    if arr[coord[0]+1][coord[1]] == pixelIntensity:  # Below
                        coordQueue.append((coord[0]+1, coord[1]))
                        arr[coord[0]+1][coord[1]] = -1

                # Right-most Edge (non-corner), compare to above, left-above, left, left-below, and below:
                elif coord[1] == arr.shape[1]-1:

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]-1][coord[1]] == pixelIntensity:  # Above
                        coordQueue.append((coord[0]-1, coord[1]))
                        arr[coord[0]-1][coord[1]] = -1

                    if arr[coord[0]-1][coord[1]-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((coord[0]-1, coord[1]-1))
                        arr[coord[0]-1][coord[1]-1] = -1

                    if arr[coord[0]][coord[1]-1] == pixelIntensity:  # Left
                        coordQueue.append((coord[0], coord[1]-1))
                        arr[coord[0]][coord[1]-1] = -1

                    if arr[coord[0]+1][coord[1]-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((coord[0]+1, coord[1]-1))
                        arr[coord[0]+1][coord[1]-1] = -1

                    if arr[coord[0]+1][coord[1]] == pixelIntensity:  # Below
                        coordQueue.append((coord[0]+1, coord[1]))
                        arr[coord[0]+1][coord[1]] = -1

                # Non-edge pixel. Compare to all pixel in neighbourhood.
                else:

                    # Store pixel coords in queue if they match,
                    # increment region size, set pixel to -1 to
                    # avoid re-checking

                    if arr[coord[0]][coord[1]-1] == pixelIntensity:  # Left
                        coordQueue.append((coord[0], coord[1]-1))
                        arr[coord[0]][coord[1]-1] = -1

                    if arr[coord[0]-1][coord[1]-1] == pixelIntensity:  # Left-Above
                        coordQueue.append((coord[0]-1, coord[1]-1))
                        arr[coord[0]-1][coord[1]-1] = -1

                    if arr[coord[0]-1][coord[1]] == pixelIntensity:  # Above
                        coordQueue.append((coord[0]-1, coord[1]))
                        arr[coord[0]-1][coord[1]] = -1

                    if arr[coord[0]-1][coord[1]+1] == pixelIntensity:  # Right-Above
                        coordQueue.append((coord[0]-1, coord[1]+1))
                        arr[coord[0]-1][coord[1]+1] = -1

                    if arr[coord[0]][coord[1]+1] == pixelIntensity:  # Right
                        coordQueue.append((coord[0], coord[1]+1))
                        arr[coord[0]][coord[1]+1] = -1

                    if arr[coord[0]+1][coord[1]+1] == pixelIntensity:  # Right-Below
                        coordQueue.append((coord[0]+1, coord[1]+1))
                        arr[coord[0]+1][coord[1]+1] = -1

                    if arr[coord[0]+1][coord[1]] == pixelIntensity:  # Below
                        coordQueue.append((coord[0]+1, coord[1]))
                        arr[coord[0]+1][coord[1]] = -1

                    if arr[coord[0]+1][coord[1]-1] == pixelIntensity:  # Left-Below
                        coordQueue.append((coord[0]+1, coord[1]-1))
                        arr[coord[0]+1][coord[1]-1] = -1

            if pixelIntensity != -1:
                glszm[pixelIntensity][regionSize] += 1

    return glszm
