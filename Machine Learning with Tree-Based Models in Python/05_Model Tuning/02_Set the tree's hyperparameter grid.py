"""
Set the tree's hyperparameter grid
In this exercise, you'll manually set the grid of hyperparameters that will be used to tune the classification tree dt and find the optimal classifier in the next exercise.

Instructions
100 XP
Define a grid of hyperparameters corresponding to a Python dictionary called params_dt with:

the key 'max_depth' set to a list of values 2, 3, and 4

the key 'min_samples_leaf' set to a list of values 0.12, 0.14, 0.16, 0.18"""
# Define params_dt
params_dt = {
             'max_depth': [2, 3, 4],
             'min_samples_leaf': [0.12, 0.14, 0.16, 0.18]
            }