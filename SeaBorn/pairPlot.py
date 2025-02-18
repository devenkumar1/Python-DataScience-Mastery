import seaborn as sns
import matplotlib.pyplot as plt
#data
tips=sns.load_dataset("tips")

# Pair plot
sns.pairplot(tips)

# Adding title
plt.suptitle("Pair Plot of Tips Dataset", y=1.02)

# Show the plot
plt.show()
