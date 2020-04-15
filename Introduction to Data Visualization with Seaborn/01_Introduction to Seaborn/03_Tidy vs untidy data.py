""""Tidy" vs. "untidy" data
Here, we have a sample dataset from a survey of children about their favorite animals. But can we use this dataset as-is with Seaborn? Let's use Pandas to import the csv file with the data collected from the survey and determine whether it is tidy, which is essential to having it work well with Seaborn.

To get you started, the filepath to the csv file has been assigned to the variable csv_filepath.

Note that because csv_filepath is a Python variable, you will not need to put quotation marks around it when you read the csv.

Instructions 1/2
50 XP
1
2
Read the csv file located at csv_filepath into a DataFrame named df.
Print the head of df to show the first five rows."""
# Import pandas
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())


"""=======================MCQ===================================="""
# Question
# View the first five rows of the DataFrame df. Is it tidy? Why or why not?

# Possible Answers
# Yes, because there are no typos or missing values.
# Yes, because it is well organized and easy to read.
# No, because a single column contains different types of information.


"""ANSWER
 No, because a single column contains different types of information."""


                    """DEVELOPER"""
                """BasitAminBhatti"""
                    """Github"""
        """https://github.com/basitaminbhatti"""