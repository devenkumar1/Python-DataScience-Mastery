import numpy as np
import matplotlib.pyplot as plt

# Data (Random matrix)
data = np.random.rand(10, 10)

# Heatmap
plt.imshow(data, cmap='coolwarm', interpolation='nearest')

# Adding labels and title
plt.title("Heatmap of Random Data")
plt.colorbar(label='Value')

# Show the plot
plt.show()
