"""Interpreting line plots
In this exercise, we'll continue to explore Seaborn's mpg dataset, which contains one row per car model and includes information such as the year the car was made, its fuel efficiency (measured in "miles per gallon" or "M.P.G"), and its country of origin (USA, Europe, or Japan).

How has the average miles per gallon achieved by these cars changed over time? Let's use line plots to find out!

Instructions 1/2
50 XP
1
2
Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "mpg" on the y-axis."""
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line")

# Show plot
plt.show()


"""========================MCQS====================="""
# Question
# Which of the following is NOT a correct interpretation of this line plot?

# Possible Answers
# The average miles per gallon has increased over time.
# The distribution of miles per gallon is smaller in 1973 compared to 1977.
# We can be 95% confident that the average miles per gallon for all cars in 1970 is between 16 and 20 miles per gallon.
# This plot assumes that our data is a random sample of all cars in the US, Europe, and Japan.

"""Answer
The distribution of miles per gallon is smaller in 1973 compared to 1977."""

                    """DEVELOPER"""
                """BasitAminBhatti"""
                    """Github"""
        """https://github.com/basitaminbhatti"""
