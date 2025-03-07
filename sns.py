import seaborn as sns

import matplotlib.pyplot as plt

# Load an example dataset
data = sns.load_dataset("iris")

# Create a scatter plot
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=data)

# Show the plot
plt.show()