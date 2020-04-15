"""
Evaluate the classification tree
Now that you've fit your first classification tree, it's time to evaluate its performance on the test set. You'll do so using the accuracy metric which corresponds to the fraction of correct predictions made on the test set.

The trained model dt from the previous exercise is loaded in your workspace along with the test set features matrix X_test and the array of labels y_test.

Instructions
100 XP
Import the function accuracy_score from sklearn.metrics.

Predict the test set labels and assign the obtained array to y_pred.

Evaluate the test set accuracy score of dt by calling accuracy_score() and assign the value to acc.

"""
# Import accuracy_score
from sklearn.metrics import accuracy_score

# Predict test set labels
y_pred = dt.predict(X_test)

# Compute test set accuracy  
acc = accuracy_score(y_test, y_pred)
print("Test set accuracy: {:.2f}".format(acc))


                    """DEVELOPER"""
                """BasitAminBhatti"""
                    """Github"""
        """https://github.com/basitaminbhatti"""