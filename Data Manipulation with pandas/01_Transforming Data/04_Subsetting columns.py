"""Subsetting columns
When working with data, you may not need all of the variables in your dataset. Square-brackets ([]) can be used to select only the columns that matter to you in an order that makes sense to you. To select only "col_a" of the DataFrame df, use

df["col_a"]
To select "col_a" and "col_b" of df, use

df[["col_a", "col_b"]]
homelessness is available and pandas is loaded as pd.

Instructions 1/3
35 XP
1
Create a DataFrame called individuals that contains only the individuals column of homelessness.
Print the head of the result."""
# Select the individuals column
individuals = homelessness["individuals"]

# Print the head of the result
print(individuals.head())

"""Create a DataFrame called state_fam that contains only the state and family_members columns of homelessness, in that order.
Print the head of the result."""
# Select the state and family_members columns
state_fam = homelessness[["state", "family_members"]]

# Print the head of the result
print(state_fam.head())

"""Create a DataFrame called ind_state that contains the individuals and state columns of homelessness, in that order.
Print the head of the result."""
# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]

# Print the head of the result
print(ind_state.head())