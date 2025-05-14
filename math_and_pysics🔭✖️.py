import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,120)
y = np.sin(x)
x2 = np.arange(0, 8, 2)


plt.plot(x,y, label = "sin(x)")
plt.plot(x,np.sqrt(x), label = "sqrt" )
plt.plot(x, np.cos(x), label = "a cos() func")
plt.axhline(0, color = "black", linewidth = 2)
plt.axvline(0, color ="Black", linewidth = 2)
plt.xlabel("Domain(y)")
plt.ylabel("Range(x)")
plt.legend()
plt.grid(True)
plt.title("My first matplotlib.pyplot plot")
plt.show()


def linear(x_value, m=-2, b=10):
    return m * x_value + b

x2 = np.arange(-1, 6, 0.1)  # Wider range to see the intercept better
y2 = linear(x2)

plt.plot(x2, y2, label="y = -2x + 10", color="blue")
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)
plt.scatter(0, linear(0), color="gold", label="Y-intercept")


plt.grid(True)
plt.legend()
plt.title("Linear Function with Intercept Highlighted")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
