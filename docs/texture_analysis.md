# Texture Analysis

- [Texture Analysis](#texture-analysis)
	- [Overview](#overview)
	- [GLCM](#glcm)
	- [GLDM](#gldm)
	- [GLRLM](#glrlm)
	- [GLSZM](#glszm)
	- [NGTDM](#ngtdm)
	- [GLCM Metrics](#glcm-metrics)


## Overview 

Texture Analysis represent an advanced statistical metric that characterizes the spatial distribution of gray-level pixels within a given vicinity. The resulting information is expressed through a matrix, serving as a foundation for deriving additional features. Although numerous texture analysis methods exist, this discussion will focus on five key texture groups: Gray Level Cooccurrence Matrix (GLCM), Gray Level Size Zone Matrix (GLSZM), Gray Level Run Length Matrix (GLRLM), Gray Level Dependence Matrix (GLDM), and Neighboring Gray Tone Difference Matrix (NGTDM). As gray level textures explore pixel arrangements, they provide valuable insights into the shapes or structures formed by the pixels.

## GLCM

The Gray Level Co-ocurrence Matrix (GLCM) elucidates the frequency of pixel intensities occurring next to each other in a specific direction, referred to as co-occurrence. It proves instrumental in discerning the organization of structures within an image. While extensively used in biomedical imagery, gray-level textures have broader applications, spanning landscape image analysis, material processing, geological property analysis, pork and beef image classification, asphalt pavement analysis, fingerprint identification, and microstructure analysis.

To construct the GLCM, comparisons are made between a central pixel and its surrounding pixels at a specified offset along the matrix direction. The resulting square matrix quantifies co-ocurrences for that direction, typically in both forward and reverse directions. Multiple directional matrices are calculated, summed, and averaged to provide an overall representation of the texture content, independent of sample orientation.

The GLCM extraction process involves mapping gray levels from the original image to a quantized image, followed by the construction of directional matrices and normalization. Parameters like means, standard deviations, marginal probabilities, and informational measures are then calculated from the normalized GLCM. These parameters contribute to the extraction of 24 texture features, which, through mathematical definitions, track the overall pixel organization in an image by quantifying relationships between pixel intensity pairs.

## GLDM

Introduced by Thibault et al. [95], GLSZM quantifies the number of different sizes of zones for each gray level in an image or region. Initially developed for cell texture quantification, it is well-suited for assessing image homogeneity, speckle-like structures, and overall structural organization. In the context of ECM images of fibrillar collagen, GLSZM reflects the clustering of collagen fibers and enables discussions on collagen bundle fragmentation. For instance, a high Small Area Emphasis feature indicates a fragmented collagen network with many small bundles, while a high Large Area Emphasis feature suggests a highly bundled collagen network.

An area of connected pixels sharing the same intensity.

Non-directional, unlike GLCM or GLRLM, eliminating the need for multiple passes and averaging to generate texture features for the entire image.

Produces a matrix \(P\) of size [M, N], where \(M\) is the number of discrete gray levels, and \(N\) is the maximum size of zones. Each element \(P(i, j)\) represents the number of zones of size \(j\) with gray level intensity \(i\).

Once constructed, the matrix is utilized to calculate features, sharing calculations with GLRLM and GLDM. Parameters are extracted before feature calculation, as detailed in Table A.3 of Appendix A. A total of 16 features are computed (see Appendix A, Table A.4), providing information about the size of structures in an image based on the size of pixel zones.

The GLSZM shares calculations with GLRLM and GLDM, as discussed later in this thesis. Several parameters are extracted before feature calculation, outlined in Table A.7 of Appendix A. Using these parameters, 15 additional features are calculated (see Table A.8), offering insights into the coarseness or fineness of structures in an image by measuring the likelihood of pixels of the same intensity being near each other.


## GLRLM

The Gray-Level Run Length Matrix (GLRLM), initially proposed by Galloway, is a set of texture features designed to analyze the run lengths of gray levels in an image. Originally applied to quantify terrain types, GLRLM is well-suited for examining linear structures within features. For instance, regions with well-organized linear structures exhibit high values for long run emphasis features. 

GLRLM counts consecutive connected pixels with the same gray intensity, known as a run, along four main directions: horizontal (0 degrees), diagonally right (45 degrees), vertically (90 degrees), and diagonally left (135 degrees). Features are then computed from each directional matrix and averaged to provide texture features for the entire image.

The construction of the GLRLM results in a matrix (P) of size [M, N], where M represents the total number of discrete gray levels, and N denotes the maximum run length found in the image. Each element P(i, j) in the GLRLM represents the number of runs of length j with gray level i in the image or region of interest.

Similar to other texture feature groups, the GLRLM is used to calculate various features, sharing calculations with the Gray Level Size Zone Matrix (GLSZM) and the Gray Level Dependence Matrix (GLDM). Extracting parameters from the matrix precedes the calculation of features.

 In essence, these textural features track linear structures in an image by evaluating the overall length of pixel runs, providing orientation information as well-oriented structures exhibit longer run lengths. 

## GLSZM


First proposed by Thibault et al. [95], the GLSZM counts the number of different sizes of zones for each gray level found in an image or region. Originally designed for cell texture quantification, it proves effective in assessing image homogeneity, speckle-like structures, and overall structural organization. In the context of analyzing fibrillar collagen from extracellular matrix (ECM) images, GLSZM captures the clustering of collagen fibers and facilitates discussions on collagen bundle fragmentation.

A zone is defined as an area of connected pixels sharing the same intensity. Unlike the Gray Level Cooccurrence Matrix (GLCM) or Gray Level Run Length Matrix (GLRLM), GLSZM is non-directional. This eliminates the need for multiple passes over an image and averaging to generate texture features for the entire image.

The GLSZM produces a matrix \(P\) of size [M, N], where \(M\) is the number of discrete gray levels found in the image or region, and \(N\) is the maximum size of the zones. Each element \(P(i, j)\) in \(I\) represents the number of zones of size \(j\) with gray level intensity \(i\). See Figure 2.10 for an illustration of the GLSZM produced by an image.

Similar to other texture feature groups, the GLSZM matrix is utilized to calculate several features. These calculations are shared with the GLRLM and the Gray Level Dependence Matrix (GLDM). Parameters are extracted before features are computed (refer to Table A.3 in Appendix A). A total of 16 features are then calculated, providing information about the size of structures in an image based on the size of pixel zones (see details in Appendix A, Table A.4).


## NGTDM
**Neighboring Gray Tone Difference Matrix (NGTDM)**

Initially proposed by Amadasun and King [99], the NGTDM is a set of texture features focusing on the intensity difference between a pixel and the average intensity of surrounding pixels. Originating from human perception of texture properties like coarseness, contrast, complexity, busyness, and strength, NGTDM finds its roots in agricultural land-use classification. Unlike methods analyzing specific structures, NGTDM evaluates how much a texture stands out from the background and how it is perceived by a human observer. In the context of ECM collagen network images, NGTDM can reveal information about the complexity of collagen networks and the strength of organized or bundled collagen fibers.

- **Neighborhood Analysis:** Similar to previous texture analysis techniques, NGTDM examines a neighborhood surrounding a central pixel.
- **Matrix Structure:** NGTDM produces a matrix with three columns: \(n_i\), \(p_i\), and \(s_i\), where \(i\) ranges from 1 to \(N\) (maximum gray tone in the image).
- **Feature Calculation:** NGTDM calculates Coarseness, Contrast, Busyness, Complexity, and Strength from the matrix.

**Feature Calculation:**

1. **Coarseness:**
   - Measures the spatial rate of change of pixel intensity across a region.
   - Calculated as: \( \text{Coarseness} = \varepsilon + \sum_{i=1}^{N} \frac{n_i s_i}{p_i} \)
   - \( \varepsilon \) prevents contrast from becoming infinite in case the summation evaluates to zero.

2. **Contrast:**
   - Measures how different regions across an image differ in average intensity.
   - Calculated as: \( \text{Contrast} = \sum_{i=1}^{N} \sum_{j=1}^{N} \frac{p_i p_j |i - j|^2}{\sum_{k=1}^{N} s_k} \)

3. **Busyness:**
   - Measures how frequently spatial changes occur between regions of an image.
   - Calculated as: \( \text{Busyness} = \frac{\sum_{i=1}^{N} n_i s_i}{\sum_{i=1}^{N} \sum_{j=1}^{N} i \cdot p_i - j \cdot p_j} \)

4. **Complexity:**
   - Measures the visual information content of a texture.
   - Calculated as: \( \text{Complexity} = \sum_{i=1}^{N} \sum_{j=1}^{N} \frac{|i - j| \cdot (p_i s_i + p_j s_j)}{N^2(p_i + p_j)} \)

5. **Strength:**
   - Measures how much a texture stands out, producing textures that are easily definable and clearly visible.
   - Calculated as: \( \text{Strength} = \frac{\sum_{i=1}^{N} \sum_{j=1}^{N} (p_i + p_j) |i - j|}{\varepsilon + \sum_{i=1}^{N} s_i} \)


## GLCM Metrics


| Parameter         | Description                                     | Definition                                             |
|-------------------|-------------------------------------------------|--------------------------------------------------------|
| \(p(i, j)\)       | Element in the normalized GLCM.                 | -                                                      |
| \(p_x(i)\)        | Marginal probabilities of rows of normalized GLCM. | \(\sum_{j=1} p(i, j)\)                                |
| \(p_y(j)\)        | Marginal probabilities of columns of normalized GLCM. | \(\sum_{i=1} p(i, j)\)                                |
| \(\mu_x\)         | Mean of normalized GLCM rows.                   | \(\sum_{i=1} i \cdot p_x(i)\)                          |
| \(\mu_y\)         | Mean of normalized GLCM columns.                | \(\sum_{j=1} j \cdot p_y(j)\)                          |
| \(\sigma_x^2\)    | Standard Deviation of normalized GLCM rows.     | \(\sum_{i=1} (i - \mu_x)^2 \cdot p_x(i)\)             |
| \(\sigma_y^2\)    | Standard Deviation of normalized GLCM columns.  | \(\sum_{j=1} (j - \mu_y)^2 \cdot p_y(j)\)             |
| \(p_{x+y}(k)\)    | Sum Probabilities of normalized GLCM.           | \(\sum_{i=1} \sum_{j=1} p(i, j) \) if \((i+j) = k\)   |
| \(p_{x-y}(k)\)    | Difference Probabilities of normalized GLCM.    | \(\sum_{i=1} \sum_{j=1} p(i, j) \) if \(|i-j| = k\)   |
| \(\mu_{x+y}\)     | Mean of sum probabilities of normalized GLCM.   | \(\sum_{k=2} k \cdot p_{x+y}(k)\)                     |
| \(\mu_{x-y}\)     | Mean of difference probabilities of normalized GLCM. | \(\sum_{k=0} k \cdot p_{x-y}(k)\)                   |
| \(H_X\)           | Entropy of marginal row probabilities.           | \(-\sum_{i=1} p_x(i) \cdot \log_2(p_x(i))\)          |
| \(H_Y\)           | Entropy of marginal column probabilities.        | \(-\sum_{j=1} p_y(j) \cdot \log_2(p_y(j))\)          |
| \(H_{XY}^2\)      | Entropy of marginal probabilities and normalized GLCM probabilities. | \(-\sum_{i=1} \sum_{j=1} p(i, j) \cdot \log_2(p_x(i) \cdot p_y(j))\) |
| \(H_{XY}^1\)      | Entropy of marginal row probabilities.           | \(-\sum_{j=1} p_y(j) \cdot \log_2(p_y(j))\)          |
| \(Q(i, j)\)       | Correlation Coefficient Matrix                  | \(\sum_{k=1} \sum_{i=1} \sum_{j=1} p(i, k) \cdot p(j, k) \) / \(\sqrt{\sum_{k=1} (\sum_{i=1} p(i, k)) \cdot (\sum_{j=1} p(j, k))}\) |
| \(p_x(i)p_y(k)\)  |                                                                    |



| Feature                | Description                                        | Definition                                           |
|------------------------|----------------------------------------------------|------------------------------------------------------|
| Autocorrelation        | Measures how often similar intensities are found as pairs. | \(\sum_{i=1} \sum_{j=1} p(i, j) \cdot i \cdot j\)     |
| Cluster Prominence     | Measures the prominence of clusters of similar pixels, or how much they stand out from background tone. | \(\sum_{i=1} \sum_{j=1} [(\mu_x - \mu_y - i - j)^4 \cdot p(i, j)]\) |
| Cluster Shade          | Measures the shade of clusters of similar pixels, or how much they stand out from background tone. | \(\sum_{i=1} \sum_{j=1} [(\mu_x - \mu_y - i - j)^3 \cdot p(i, j)]\) |
| Cluster Tendency       | Measures the tendency of clusters of similar pixels, or how much they stand out from background tone. | \(\sum_{i=1} \sum_{j=1} [(\mu_x - \mu_y - i - j)^2 \cdot p(i, j)]\) |
| Contrast               | Measures gray level variation.                    | \(\sum_{i=1} \sum_{j=1} |i - j|^2 \cdot p(i, j)\)    |
| Correlation            | Measures the relationship between average gray levels. | \(\frac{\sum_{i=1} \sum_{j=1} (i - \mu_x) (j - \mu_y) p(i, j)}{\sigma_x \sigma_y}\) |
| Difference Entropy     | Measures entropy of difference probabilities.     | \(-\sum_{k=0} px-y(k) \cdot \log_2(px-y(k))\)       |
| Difference Variance    | Measures variance in difference probabilities.   | \(\sum_{k=0} (k - \mu_{x-y}) \cdot px-y(k)\)         |
| Dissimilarity          | Measures how dissimilar pixel pairs are.          | \(\sum_{i=1} \sum_{j=1} \|i - j\|^{2} \cdot p(i, j)\)      |

| Feature                    | Description                                       | Definition                                           |
|----------------------------|---------------------------------------------------|------------------------------------------------------|
| Energy                     | Measures how often similar pixel values are found together, or a measure of ‘orderliness’. | \(\sum_{i=1} \sum_{j=1} p(i, j)^2\)                   |
| Entropy                    | Measures how disordered the GLCM is, or how random pixel pairs are. | \(-\sum_{i=1} \sum_{j=1} p(i, j) \cdot \log_2(p(i, j))\) |
| Homogeneity 1              | Measure of similarity between gray level pairs.    | \(\sum_{i=1} \sum_{j=1} \frac{p(i, j)}{1 + |i - j|}\)  |
| Homogeneity 2              | Measure of similarity between gray level pairs.    | \(\sum_{i=1} \sum_{j=1} \frac{p(i, j)}{1 + |i - j|^2}\) |
| Information Measure of Correlation 1 | Measure of correlation between gray level pairs. | \(\frac{HXY - HXY_1}{\max(HX, HY)}\) |
| Information Measure of Correlation 2 | Measure of correlation between gray level pairs. | \(\sqrt{1 - e^{-2(HXY_2 - HXY_1)}}\) |
| Inverse Difference Moment Normalized | Measure of homogeneity, normalized.               | \(\sum_{i=1} \sum_{j=1} \frac{p(i, j)}{1 + \left(\frac{|i - j|}{N}\right)^2}\) |
| Maximum Probability         | Maximum probability of gray level pairs.          | \(\max(p(i, j))\)                                   |
| Sum Average                | Average of summed diagonal probabilities.         | \(\sum_{k=2} k \cdot px+y(k)\)                      |
| Sum Entropy                | Entropy, or disorder, of summed diagonal probabilities. | \(-\sum_{k=2} px+y(k) \cdot \log_2(px+y(k))\)      |
| Sum Variance               | Variance of summed diagonal probabilities.        | \(\sum_{k=2} (k - \mu_{x+y}) \cdot px+y(k)\)         |
