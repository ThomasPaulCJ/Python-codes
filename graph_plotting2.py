import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 7, 100)
y = x**4 + 5

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = x^4 + 5')
plt.grid(True)
plt.show()
plt.figure()
plt.stem(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Stem Graph of y = x^4 + 5')
plt.grid(True)
plt.show()
plt.bar(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bar Graph of y = x^4 + 5')
plt.grid(True)
plt.show()
