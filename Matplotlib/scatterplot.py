import matplotlib.pyplot as plt

#data
x=[1,2,3,4,5]
y=[1,4,9,16,25]

plt.scatter(x,y,color="red",label="y=x^2")
plt.title("scatter plot of x vs y")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()