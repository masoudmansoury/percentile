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

Experiments are performed on multiple algorithms and datasets. For sensitivity analysis, we also performed a grid-search over below hyperparamters:

| hyperparamter            | value                              |
| -------------------------|:----------------------------------:|
| overall bias             | {0.0001, 0.001, 0.005, 0.01}       |
| user bias                | {0.0001, 0.001, 0.005, 0.01}       |
| item bias                | {0.0001, 0.001, 0.005, 0.01}       |
| implicit feedback bias   | {0.0001, 0.001, 0.005, 0.01}       |
| learning rate            | {0.0001, 0.001, 0.005, 0.01}       |
| number of iterations     | {30, 50, 100}                      |
| number of factors        | {50, 100, 150}                     |
| number of neighbors      | {10, 20, 30, 40, 50, 70, 100, 200} |
| shrinkage                | {0, 10, 20}                        |
| similarity function      | {pearson, cosine}                  |
| percentile smoothed param| {5, 10, 20}                  |

The results for all algorithms that we experimented are as follow:

#### Bookcrossing dataset

| algorithm     | rating   | z-score  | percentile first | percentile median | percentile last | smoothed first | smoothed median | smoothed last |
| ------------- |:--------:| --------:|:----------------:|:-----------------:|:---------------:|:--------------:|:---------------:|:-------------:|
| BiasedMF      | 0.009    | 0.008    | **0.014**        | **0.014**         | **0.012**       | 0.014          | 0.014           | 0.013         |
| SVD++         | 0.009    | 0.006    | **0.011**        | **0.011**         | **0.010**       | 0.014          | 0.013           | 0.012         |
| UserKNN       | 0.015    | 0.016    | 0.016            | 0.016             | 0.016           | 0.016          | 0.016           | 0.016         |
| ItemKNN       | 0.059    | 0.059    | **0.061**        | **0.061**         | **0.061**       | 0.061          | 0.061           | 0.061         |
| NMF           | 0.0005   | 0.0004   | 0.0005           | **0.0006**        | **0.0007**      | 0.0005         | **0.0006**      | **0.0006**    |

#### CiaoDVD dataset

| algorithm     | rating   | z-score  | percentile first | percentile median | percentile last | smoothed first | smoothed median | smoothed last |
| ------------- |:--------:| --------:|:----------------:|:-----------------:|:---------------:|:--------------:|:---------------:|:-------------:|
| BiasedMF      | 0.019    | 0.005    | **0.027**        | **0.024**         | 0.016           | **0.027**      | **0.027**       | **0.026**     |
| SVD++         | 0.009    | 0.011    | **0.022**        | **0.019**         | **0.017**       | **0.019**      | **0.018**       | **0.016**     |
| UserKNN       | 0.0097   | 0.0099   | 0.0097           | 0.0098            | 0.0097          | **0.010**      | **0.010**       | **0.010**     |
| ItemKNN       | 0.034    | 0.034    | 0.033            | 0.033             | 0.034           | 0.033          | 0.034           | 0.034         |
| NMF           | 0.0001   | 0.0001   | 0.0001           | 0.0001            | 0.0001          | 0.0001         | 0.0001          | 0.0001        |

#### FilmTrust dataset

| algorithm     | rating   | z-score  | percentile first | percentile median | percentile last | smoothed first | smoothed median | smoothed last |
| ------------- |:--------:| --------:|:----------------:|:-----------------:|:---------------:|:--------------:|:---------------:|:-------------:|
| BiasedMF      | 0.078    | 0.092    | **0.317**        | **0.314**         | **0.302**       | **0.352**      | **0.345**       | **0.335**     |
| SVD++         | 0.049    | 0.072    | **0.079**        | **0.087**         | **0.124**       | **0.081**      | **0.092**       | **0.102**     |
| UserKNN       | 0.543    | 0.544    | 0.543            | 0.542             | 0.542           | 0.543          | 0.544           | 0.543         |
| ItemKNN       | 0.537    | 0.563    | 0.503            | 0.503             | 0.489           | 0.496          | 0.497           | 0.485         |
| NMF           | 0.0005   | 0.0004   | **0.0068**       | **0.0030**        | **0.0018**      | **0.0009**     | **0.0006**      | **0.0007**    |

#### MovieLens1M dataset

| algorithm     | rating   | z-score  | percentile first | percentile median | percentile last | smoothed first | smoothed median | smoothed last |
| ------------- |:--------:| --------:|:----------------:|:-----------------:|:---------------:|:--------------:|:---------------:|:-------------:|
| BiasedMF      | 0.116    | 0.116    | **0.151**        | **0.156**         | **0.156**       | **0.157**      | **0.158**       | **0.156**     |
| SVD++         | 0.145    | 0.145    | **0.153**        | **0.157**         | **0.153**       | **0.162**      | **0.166**       | **0.157**     |
| UserKNN       | 0.219    | 0.219    | 0.219            | 0.219             | 0.217           | 0.116          | 0.117           | 0.117         |
| ItemKNN       | 0.260    | 0.272    | 0.254            | **0.275**         | 0.267           | 0.0007         | 0.0007          | 0.0007        |
| NMF           | 0.0046   | 0.0073   | 0.0071           | 0.0052            | 0.0048          | 0.0009         | 0.0006          | 0.0014        |

### Miscellaneous

Please send any questions you might have about the code to <mmansou4@depaul.edu>.
