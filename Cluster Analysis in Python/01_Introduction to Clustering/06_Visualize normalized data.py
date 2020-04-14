"""
Visualize normalized data
After normalizing your data, you can compare the scaled data to the original data to see the difference. The variables from the last exercise, goals_for and scaled_data are already available to you.

Instructions
100 XP
Use the matplotlib library to plot the original and scaled data.
Show the legend in the plot.
Display the plot.
"""
# Plot original data
plt.plot(goals_for, label='original')

# Plot scaled data
plt.plot(scaled_data, label='scaled')

# Show the legend in the plot
plt.legend()

# Display the plot
plt.show()