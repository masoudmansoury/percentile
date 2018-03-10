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


### Miscellaneous

Please send any questions you might have about the code to <mmansou4@depaul.edu>.
