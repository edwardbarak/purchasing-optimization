# Ad Purchasing Optimization

## Problem
You have sufficient enough budget next month to buy a total of 10 ads spread across 6 different regions, with each ad costing $0.5 million. Your company's marketing analytics team has prepared a study predicting that the net sales S (in millions of dollars) in each region should be given by the formula:

> S = A-Be^(-Cd)

Where d is the number of ads purchased in region 1. and A.B.C are constants as specified in
the following table:

R = region A, B, C = constants

R [1, 2, 3, 4, 5, 6]
A [4.1, 8.2, 6.9, 2.3, 4.4, 5.2]
B [2.1, 4.3, 3.2, 1.9, 2.2, 3.1]
C [0.4, 0.3, 0.2, 0.6, 0.4, 0.3]


You would like to maximize your total predicted profit, which is the sum of the predicted net sales
from all regions, minus the amount spent purchasing ads.

**Compute the pattern of ad purchases that maximizes total predicted profit.**

## Approach
Calculate all possible combinations of possible ad purchasing patterns, and map the given function across those combinations.

## Results

**Maximum Profit:** $16.6153776748425 million.

**Region 1:** 1 ad(s)
**Region 2:** 3 ad(s)
**Region 3:** 1 ad(s)
**Region 4:** 1 ad(s)
**Region 5:** 1 ad(s)
**Region 6:** 2 ad(s)

**Total ad(s) bought:** 9

> Code in *optmizeAds.py*