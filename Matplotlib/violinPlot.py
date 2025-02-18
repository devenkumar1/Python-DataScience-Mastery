import numpy as np
import matplotlib.pyplot as plt
# Data
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Violin plot
plt.violinplot(data)

# Adding labels and title
plt.title("Violin Plot")
plt.xlabel("Category")
plt.ylabel("Value")

# Show the plot
plt.show()
