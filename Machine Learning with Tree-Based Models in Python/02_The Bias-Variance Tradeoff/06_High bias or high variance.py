"""=========================MCQ========================="""
"""
High bias or high variance?
In this exercise you'll diagnose whether the regression tree dt you trained in the previous exercise suffers from a bias or a variance problem.

The training set RMSE (RMSE_train) and the CV RMSE (RMSE_CV) achieved by dt are available in your workspace. In addition, we have also loaded a variable called baseline_RMSE which corresponds to the root mean-squared error achieved by the regression-tree trained with the disp feature only (it is the RMSE achieved by the regression tree trained in chapter 1, lesson 3). Here baseline_RMSE serves as the baseline RMSE above which a model is considered to be underfitting and below which the model is considered 'good enough'.

Does dt suffer from a high bias or a high variance problem?"""

# Possible Answers
# dt suffers from high variance because RMSE_CV is far less than RMSE_train.

# dt suffers from high bias because RMSE_CV ≈ RMSE_train and both scores are greater than baseline_RMSE.

# dt is a good fit because RMSE_CV ≈ RMSE_train and both scores are smaller than baseline_RMSE.

"""ANSWER
dt suffers from high bias because RMSE_CV ≈ RMSE_train and both scores are greater than baseline_RMSE.
"""
