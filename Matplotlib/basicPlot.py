import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

#line plot
plt.plot(x,y,label="y=x^2",color="red",marker="o")
plt.title("Line Plot of y = x^2")
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend()
plt.show()
