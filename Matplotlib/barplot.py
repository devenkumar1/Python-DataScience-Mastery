import matplotlib.pyplot as plt
#data
categories=["A","B","A","B","B"]
value=[23,34,56,78,65]

plt.bar(categories,value,color="#EB45")

plt.title("bar plot of different categories")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()