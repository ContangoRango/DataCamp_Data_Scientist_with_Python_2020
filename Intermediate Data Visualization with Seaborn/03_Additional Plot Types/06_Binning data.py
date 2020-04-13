"""
Binning data
When the data on the x axis is a continuous value, it can be useful to break it into different bins in order to get a better visualization of the changes in the data.

For this exercise, we will look at the relationship between tuition and the Undergraduate population abbreviated as UG in this data. We will start by looking at a scatter plot of the data and examining the impact of different bin sizes on the visualization.

Instructions 1/3
30 XP
1
2
3
Create a regplot of Tuition and UG and set the fit_reg parameter to False to disable the regression line.
"""
# Create a scatter plot by disabling the regression line
sns.regplot(data=df,
            y='Tuition',
            x="UG",
            fit_reg=False)

plt.show()
plt.clf()

"""Create another plot with the UG data divided into 5 bins."""
# Create a scatter plot and bin the data into 5 bins
sns.regplot(data=df,
            y='Tuition',
            x="UG",
            x_bins=5)

plt.show()
plt.clf()

"""Create a regplot() with the data divided into 8 bins."""
# Create a regplot and bin the data into 8 bins
sns.regplot(data=df,
            y='Tuition',
            x="UG",
            x_bins=8)

plt.show()
plt.clf()