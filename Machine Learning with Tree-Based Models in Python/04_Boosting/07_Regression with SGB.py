"""
Regression with SGB
As in the exercises from the previous lesson, you'll be working with the Bike Sharing Demand dataset. In the following set of exercises, you'll solve this bike count regression problem using stochastic gradient boosting.

Instructions
100 XP
Instantiate a Stochastic Gradient Boosting Regressor (SGBR) and set:

max_depth to 4 and n_estimators to 200,

subsample to 0.9, and

max_features to 0.75.

"""
# Import GradientBoostingRegressor
from sklearn.ensemble import GradientBoostingRegressor

# Instantiate sgbr
sgbr = GradientBoostingRegressor(max_depth=4, 
                                 subsample=0.9,
                                 max_features=0.75,
                                 n_estimators=200,                                
                                 random_state=2)