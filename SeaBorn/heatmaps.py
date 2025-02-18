import seaborn as sns
import matplotlib.pyplot as plt
# Data
tips = sns.load_dataset("tips")


# Data
flights = sns.load_dataset("flights")

# Pivot the data for heatmap
pivot_flights = flights.pivot_table(index="month", columns="year", values="passengers")

# Heatmap
sns.heatmap(pivot_flights, annot=True, cmap="YlGnBu", fmt="d")

# Adding labels and title
plt.title("Heatmap of Passengers Over Months and Years")
plt.xlabel("Year")
plt.ylabel("Month")

# Show the plot
plt.show()
