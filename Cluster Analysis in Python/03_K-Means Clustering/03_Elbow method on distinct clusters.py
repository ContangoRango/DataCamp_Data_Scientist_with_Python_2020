"""
Elbow method on distinct clusters
Let us use the comic con data set to see how the elbow plot looks on a data set with distinct, well-defined clusters. You may want to display the data points before proceeding with the exercise.

The data is stored in a Pandas data frame, comic_con. x_scaled and y_scaled are the column names of the standardized X and Y coordinates of people at a given point in time.

Instructions 1/2
50 XP
1
2
Create a list of distortions for each cluster in num_clusters.
Create a data frame elbow_plot with num_clusters and distortions.
With the .lineplot() method, plot elbow_plot with num_clusters in the x axis and distortions in the y axis.
"""
distortions = []
num_clusters = range(1, 7)

# Create a list of distortions from the kmeans function
for i in num_clusters:
    cluster_centers, distortion = kmeans(comic_con[['x_scaled', 'y_scaled']], i)
    distortions.append(distortion)

# Create a data frame with two lists - num_clusters, distortions
elbow_plot = pd.DataFrame({'num_clusters': num_clusters, 'distortions': distortions})

# Creat a line plot of num_clusters and distortions
sns.lineplot(x='num_clusters', y='distortions', data = elbow_plot)
plt.xticks(num_clusters)
plt.show()


"""==================MCQ===================="""
# Question
# From the elbow plot, how many clusters are there in the data?

# Possible Answers
# 2 clusters
# 4 clusters
# 6 clusters

"""Answers
 2 clusters"""



                     """DEVELOPER"""
                """BasitAminBhatti"""
                    """Github""""
        """https://github.com/basitaminbhatti"""