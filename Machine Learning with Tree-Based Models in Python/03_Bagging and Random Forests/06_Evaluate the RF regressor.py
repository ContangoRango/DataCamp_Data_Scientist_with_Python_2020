"""
Evaluate the RF regressor
You'll now evaluate the test set RMSE of the random forests regressor rf that you trained in the previous exercise.

The dataset is processed for you and split into 80% train and 20% test. The features matrix X_test, as well as the array y_test are available in your workspace. In addition, we have also loaded the model rf that you trained in the previous exercise.

Instructions
100 XP
Import mean_squared_error from sklearn.metrics as MSE.
Predict the test set labels and assign the result to y_pred.
Compute the test set RMSE and assign it to rmse_test."""
# Import mean_squared_error as MSE
from sklearn.metrics import mean_squared_error as MSE

# Predict the test set labels
y_pred = rf.predict(X_test)

# Evaluate the test set RMSE
rmse_test = MSE(y_test, y_pred)**(1/2)

# Print rmse_test
print('Test set RMSE of rf: {:.2f}'.format(rmse_test))



                    """DEVELOPER"""
                """BasitAminBhatti"""
                    """Github"""
        """https://github.com/basitaminbhatti"""