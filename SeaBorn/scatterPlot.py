import seaborn as sns
import matplotlib.pyplot as plt

# Data
tips = sns.load_dataset("tips")

# Scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips)

# Adding labels and title
plt.title("Scatter Plot of Total Bill vs Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")

# Show the plot
plt.show()
