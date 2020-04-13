"""Creating Custom Palettes
Choosing a cohesive palette that works for your data can be time consuming. Fortunately, Seaborn has several functions that allow you to create your own custom sequential, categorical, or diverging palettes. Seaborn also makes it easy to see your palettes by using the palplot() function.

In this exercise, you can experiment with creating different palettes.

Instructions 1/3
30 XP
1
Create and display a Purples sequential palette containing 8 colors.

"""
# Create the Purples palette
sns.palplot(sns.color_palette("Purples", 8))
plt.show()

"""Create and display a palette with 10 colors using the husl system."""
# Create the husl palette
sns.palplot(sns.color_palette("husl", 10))
plt.show()

"""Create and display a diverging palette with 6 colors coolwarm."""
# Create the coolwarm palette
sns.palplot(sns.color_palette("coolwarm", 6))
plt.show()