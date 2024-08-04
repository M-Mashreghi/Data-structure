import numpy as np
import matplotlib.pyplot as plt

# Generate a grid of values for x, y (which will also represent v1, v2)
x = np.linspace(0, 400, 400)  # Adjusted range
y = np.linspace(0, 400, 400)
X, Y = np.meshgrid(x, y)

# Calculate the inequalities
inequality1 = 2 * X + Y <= 100
inequality2 = X + 2 * Y <= 100

# Plot the regions satisfying the inequalities
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, inequality1, levels=1, colors='red', alpha=0.5)  # Light blue for the first inequality
plt.contourf(X, Y, inequality2, levels=1, colors='blue', alpha=0.5)  # Light green for the second inequality
plt.title('Regions where 2x + y <= 100 and v1 + 2v2 <= 100')
plt.xlabel('x, v1')
plt.ylabel('y, v2')
plt.colorbar(label='Valid regions (1 = True, 0 = False)')
plt.grid(True)
plt.show()
