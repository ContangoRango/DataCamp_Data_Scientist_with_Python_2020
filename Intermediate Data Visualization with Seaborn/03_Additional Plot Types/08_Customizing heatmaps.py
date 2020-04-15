"""
Customizing heatmaps
Seaborn supports several types of additional customizations to improve the output of a heatmap. For this exercise, we will continue to use the Daily Show data that is stored in the df variable but we will customize the output.

Instructions
100 XP
Create a crosstab table of Group and YEAR
Create a heatmap of the data using the BuGn palette
Disable the cbar and increase the linewidth to 0.3"""
# Create the crosstab DataFrame
pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])

# Plot a heatmap of the table
sns.heatmap(pd_crosstab, cbar=False, cmap="BuGn", linewidths=.3)

# Rotate tick marks for visibility
plt.yticks(rotation=0)
plt.xticks(rotation=90)

# Show the plot
plt.show()
plt.clf()


                    """DEVELOPER"""
                """BasitAminBhatti"""
                    """Github""""
        """https://github.com/basitaminbhatti"""