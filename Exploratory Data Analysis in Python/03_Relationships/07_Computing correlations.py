"""Computing correlations
The purpose of the BRFSS is to explore health risk factors, so it includes questions about diet. The variable '_VEGESU1' represents the number of servings of vegetables respondents reported eating per day.

Let's see how this variable relates to age and income.

Instructions
100 XP
From the brfss DataFrame, select the columns 'AGE', 'INCOME2', and '_VEGESU1'.
Compute the correlation matrix for these variables."""
# Select columns
columns = ['AGE', 'INCOME2', '_VEGESU1']
subset = brfss[columns]

# Compute the correlation matrix
print(subset.corr())