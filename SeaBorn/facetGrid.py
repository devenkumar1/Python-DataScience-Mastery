import seaborn as sns
import matplotlib.pyplot as plt
# Data
tips = sns.load_dataset("tips")


# FacetGrid
g = sns.FacetGrid(tips, col="sex", row="time")
g.map(sns.scatterplot, "total_bill", "tip")

# Adding labels and title
g.set_axis_labels("Total Bill ($)", "Tip ($)")
g.set_titles(col_template="{col_name} Dining", row_template="{row_name} Time")

# Show the plot
plt.show()
