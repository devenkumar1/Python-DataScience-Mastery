import numpy as np
import matplotlib.pyplot as plt
# Data
x = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]
y2 = [2, 3, 4, 5, 6]

# Area plot
plt.fill_between(x, y1, color="skyblue", alpha=0.4, label="Area 1")
plt.fill_between(x, y2, color="orange", alpha=0.4, label="Area 2")

# Adding labels and title
plt.title("Area Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()

# Show the plot
plt.show()
