import seaborn as sns
import matplotlib.pyplot as plt

data=tips = sns.load_dataset("tips")

# Bar plot
sns.barplot(x="day", y="total_bill", data=tips)

# Adding labels and title
plt.title("Bar Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")

# Show the plot
plt.show()
