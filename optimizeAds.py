from math import e
from itertools import combinations_with_replacement
import numpy as np

def projection(d, adCost, table):
    # map regional ad purchases to formula
    ttl = 0
    for i in range(6):
        ttl += table[i][0] - table[i][1] * pow(e,float(-1)*table[i][2]*d.count(str(i))) # formula from marketing analytics
    
    netProfit = ttl - (len(d) - d.count('6')) * adCost
    return netProfit

a = np.array([4.1, 8.2, 6.9, 2.3, 4.4, 5.2])
b = np.array([2.1, 4.3, 3.2, 1.9, 2.2, 3.1])
c = np.array([0.4, 0.3, 0.2, 0.6, 0.4, 0.3])

stages = 6
budget = 10
adCost = 0.5

table = np.array([a, b, c]).T # Create table for constants
comboChoices = ''.join([str(i) for i in range(stages+1)]) # possible regional choices

combos = [''.join(combo) for combo in list(combinations_with_replacement(comboChoices, budget))] # All possible combinations of purchasing ads
results = [(combo, projection(combo, adCost, table)) for combo in combos] # apply projection() to every possible ad purchasing combination
maxProfit = sorted(results, key=lambda x:x[1], reverse=True)[0] # get the maximum result

print('Maximum Profit: ${} million.\n'.format(maxProfit[1]))

print('{} ad(s) in region 1'.format(maxProfit[0].count('0')))
print('{} ad(s) in region 2'.format(maxProfit[0].count('1')))
print('{} ad(s) in region 3'.format(maxProfit[0].count('2')))
print('{} ad(s) in region 4'.format(maxProfit[0].count('3')))
print('{} ad(s) in region 5'.format(maxProfit[0].count('4')))
print('{} ad(s) in region 6'.format(maxProfit[0].count('5')))
print('\nTotal ad(s) bought: {}'.format(len(maxProfit[0]) - maxProfit[0].count('6')))