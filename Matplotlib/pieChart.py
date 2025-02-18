import matplotlib.pyplot as plt
labels=["A","B","C","D"]
sizes=[20,30,10,40]


plt.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=0)

plt.title("proportions of A,B,C,D")
plt.show()