import matplotlib.pyplot as plt
import seaborn as sns
#data
tips=sns.load_dataset("tips")


# Regression plot
sns.regplot(x="total_bill", y="tip", data=tips)

# Adding labels and title
plt.title("Regression Plot of Total Bill vs Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")

# Show the plot
plt.show()
