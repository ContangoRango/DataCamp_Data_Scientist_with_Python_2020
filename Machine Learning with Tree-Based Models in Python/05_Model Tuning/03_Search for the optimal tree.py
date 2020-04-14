"""
Search for the optimal tree
In this exercise, you'll perform grid search using 5-fold cross validation to find dt's optimal hyperparameters. Note that because grid search is an exhaustive process, it may take a lot time to train the model. Here you'll only be instantiating the GridSearchCV object without fitting it to the training set. As discussed in the video, you can train such an object similar to any scikit-learn estimator by using the .fit() method:

grid_object.fit(X_train, y_train)
An untuned classification tree dt as well as the dictionary params_dt that you defined in the previous exercise are available in your workspace.

Instructions
100 XP
Instructions
100 XP
Import GridSearchCV from sklearn.model_selection.

Instantiate a GridSearchCV object using 5-fold CV by setting the parameters:

estimator to dt, param_grid to params_dt and

scoring to 'roc_auc'."""
# Import GridSearchCV
from sklearn.model_selection import GridSearchCV

# Instantiate grid_dt
grid_dt = GridSearchCV(estimator=dt,
                       param_grid=params_dt,
                       scoring='roc_auc',
                       cv=5,
                       n_jobs=-1)