import seaborn as sns
import matplotlib.pyplot as plt
# Data
tips = sns.load_dataset("tips")


# Violin plot
sns.violinplot(x="day", y="total_bill", data=tips)

# Adding labels and title
plt.title("Violin Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")

# Show the plot
plt.show()
