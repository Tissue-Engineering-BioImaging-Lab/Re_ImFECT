
import os as os
import csv
import skimage as ski
from dev.lib.matrixCalc.matrixGLCM import calc_glcm
from dev.lib.metricCalc.glcmMetrics import calcGLCMMetrics


def main() -> None:

    glcm_field_names: list[str] = [
        "GLCM - Autocorrelation",
        "GLCM - Cluster Prominence",
        "GLCM - Cluster Shade",
        "GLCM - Cluster Tendency",
        "GLCM - Contrast",
        "GLCM - Correlation",
        "GLCM - Difference Average",
        "GLCM - Difference Variance",
        "GLCM - Difference Entropy",
        "GLCM - Joint Average",
        "GLCM - Joint Energy",
        "GLCM - Joint Entropy",
        "GLCM - Homogeneity",
        "GLCM - Informational Measure of Correlation 1",
        "GLCM - Informational Measure of Correlation 2",
        "GLCM - Maximal Correlation Coefficient",
        "GLCM - Inverse Difference Moment",
        "GLCM - Inverse Difference Moment Normalized",
        "GLCM - Inverse Difference",
        "GLCM - Inverse Difference Normalized",
        "GLCM - Inverse Variance",
        "GLCM - Maximum Probability",
        "GLCM - Sum Average",
        "GLCM - Sum Entropy",
        "GLCM - Sum Of Squares"
    ]

    input_dir_path: str = "./images/7293_11M_NA/"
    output_dir_path: str = "./results/7293_11M_NA/"

    os.mkdir(output_dir_path) if not os.path.exists(output_dir_path) else None

    list_images: list[str] = os.listdir(input_dir_path)

    for file_name in list_images:

        image: Any = ski.io.imread(input_dir_path+file_name, as_gray=True)

        glcm_matrix: NDArray[float64] = calc_glcm(image, angle=0, bitDepth=8)

        features: dict[str, int] = calcGLCMMetrics(glcm_matrix)

        with open(
            output_dir_path+file_name+"-glcm-features.csv", "w", newline=''
        ) as result_file:

            csv_file: _writer = csv.DictWriter(
                result_file, fieldnames=glcm_field_names
            )
            csv_file.writeheader()
            csv_file.writerow(features)


if __name__ == "__main__":
    main()
