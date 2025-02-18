import numpy as np
import matplotlib.pyplot as plt

#data
data=[np.random.normal(0,1,100) for _ in range(4)]

#boxplot
plt.boxplot(data, vert=True, patch_artist=True)

# Adding labels and title
plt.title("Box Plot of 4 Different Data Sets")
plt.xlabel("Data Sets")
plt.ylabel("Value")

# Show the plot
plt.show()