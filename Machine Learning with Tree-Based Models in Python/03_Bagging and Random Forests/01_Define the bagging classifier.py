"""
Define the bagging classifier
In the following exercises you'll work with the Indian Liver Patient dataset from the UCI machine learning repository. Your task is to predict whether a patient suffers from a liver disease using 10 features including Albumin, age and gender. You'll do so using a Bagging Classifier.

Instructions
100 XP
Import DecisionTreeClassifier from sklearn.tree and BaggingClassifier from sklearn.ensemble.

Instantiate a DecisionTreeClassifier called dt.

Instantiate a BaggingClassifier called bc consisting of 50 trees."""
# Import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier

# Import BaggingClassifier
from sklearn.ensemble import BaggingClassifier

# Instantiate dt
dt = DecisionTreeClassifier(random_state=1)

# Instantiate bc
bc = BaggingClassifier(base_estimator=dt, n_estimators=50, random_state=1)