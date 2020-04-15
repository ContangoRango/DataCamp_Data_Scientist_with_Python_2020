"""
Comparing styles
Seaborn supports setting different styles that can control the aesthetics of the final plot. In this exercise, you will plot the same data in two different styles in order to see how the styles change the output.

Instructions 1/2
50 XP
1
Create a distplot() of the fmr_2 column using a dark style. After showing the plot, use plt.clf() to clear the figure."""
# Plot with a dark style 
sns.set_style('dark')
sns.distplot(df['fmr_2'])
plt.show()

# Clear the figure
plt.clf()


"""Create the same distplot() of fmr_2 using a whitegrid style. Clear the plot after showing it."""
# Plot with a whitegrid style
sns.set_style('whitegrid')
sns.distplot(df['fmr_2'])
plt.show()

# Clear the figure
plt.clf()


                    """DEVELOPER"""
                """BasitAminBhatti"""
                    """Github""""
        """https://github.com/basitaminbhatti"""