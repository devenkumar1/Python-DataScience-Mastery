import numpy as np
import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
data1 = [10, 20, 30, 40]
data2 = [15, 25, 35, 45]

# Stacked bar plot
plt.bar(categories, data1, label='Data 1', color='blue')
plt.bar(categories, data2, bottom=data1, label='Data 2', color='orange')

# Adding labels and title
plt.title("Stacked Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.legend()

# Show the plot
plt.show()
