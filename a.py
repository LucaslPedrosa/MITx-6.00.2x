import matplotlib
matplotlib.use('TkAgg') # O 'use' vem daqui!
import matplotlib.pyplot as plt
import numpy as np
# Generate data: a simple random walk
# Starting at 0, adding random steps between -1 and 1
steps = 1000
data = np.cumsum(np.random.uniform(-1, 1, steps))

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(data, label='Random Walk', color='#1f77b4', linewidth=1.5)

# Formatting the graph
plt.title('Stochastic Process: Random Walk Test', fontsize=14)
plt.xlabel('Steps', fontsize=12)
plt.ylabel('Position', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Display the plot
plt.show()
