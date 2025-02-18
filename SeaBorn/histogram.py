import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")


# Histogram
sns.histplot(tips["total_bill"], kde=True, color="blue")

# Adding labels and title
plt.title("Histogram of Total Bill")
plt.xlabel("Total Bill ($)")
plt.ylabel("Frequency")

# Show the plot
plt.show()
