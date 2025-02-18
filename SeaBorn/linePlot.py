import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
# Line plot
sns.lineplot(x="day", y="total_bill", data=tips)

# Adding labels and title
plt.title("Line Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")

# Show the plot
plt.show()
