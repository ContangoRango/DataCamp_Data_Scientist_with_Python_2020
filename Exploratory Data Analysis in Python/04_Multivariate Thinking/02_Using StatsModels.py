"""
Using StatsModels
Let's run the same regression using SciPy and StatsModels, and confirm we get the same results.

Instructions
0 XP
Compute the regression of '_VEGESU1' as a function of 'INCOME2' using SciPy's linregress().
Compute the regression of '_VEGESU1' as a function of 'INCOME2' using StatsModels' smf.ols().
"""
from scipy.stats import linregress
import statsmodels.formula.api as smf

# Run regression with linregress
subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']
res = linregress(xs, ys)
print(res)

# Run regression with StatsModels
results = smf.ols('_VEGESU1 ~ INCOME2', data=brfss).fit()
print(results.params)