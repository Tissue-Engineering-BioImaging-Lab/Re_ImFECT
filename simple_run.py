
import os as os
import skimage as ski
from dev.lib.matrixCalc.matrixGLCM import calc_glcm


def main():

    dir_path = "./images/7293_11M_NA/"

    list_images = os.listdir(dir_path)

    image = ski.io.imread(dir_path+list_images[0], as_gray=True)
    matrix = calc_glcm(image, angle=0, bitDepth=8)
    print(matrix)


if __name__ == "__main__":
    main()
