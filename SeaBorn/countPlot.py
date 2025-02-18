import seaborn as sns
import matplotlib.pyplot as plt
# Data
tips = sns.load_dataset("tips")


# Count plot
sns.countplot(x="day", data=tips)

# Adding labels and title
plt.title("Count Plot of Days")
plt.xlabel("Day")
plt.ylabel("Count")

# Show the plot
plt.show()
