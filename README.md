# Percentile Computation

This repository provides a reference implementation of percentile transformation for user ratings in recommender systems.  

### Basic usage 

#### Input

The supported format is ratings provided by users on items:

	userid itemid rating

Columns are tab-separated.

#### Output

The output file has the same format as the input file except the last column which consists of computed percentile values:

	userid itemid percentile

### Results

The results for all algorithms that we experimented are as follow:

#### Bookcrossing dataset

| algorithm     | rating   | z-score  | percentile first | percentile median | percentile last |
| ------------- |:--------:| --------:|:----------------:|:-----------------:|:---------------:|
| ItemAVG       | 0.00047  | 0.00042  | **0.00054**      | **0.00057**       | **0.00071**     |
| BiasedMF      | 0.009    | 0.008    | **0.014**        | **0.014**         | **0.012**       |
| SVD++         | 0.009    | 0.006    | **0.011**        | **0.011**         | **0.010**       |
| UserKNN       | 0.015    | 0.016    | 0.016            | 0.016             | 0.016           |
| ItemKNN       | 0.059    | 0.059    | **0.061**        | **0.061**         | **0.061**       |
| NMF           | 0.0005   | 0.0004   | 0.0005           | **0.0006**        | **0.0007**      |

### Miscellaneous

Please send any questions you might have about the code to <mmansou4@depaul.edu>.
