import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

def demonstrate_matplotlib():
    """
    Function to demonstrate multiple ways of plotting with Matplotlib.
    """
    
    # --- 1. DATA PREPARATION ---
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    categories = ['A', 'B', 'C', 'D']
    values = [15, 30, 45, 10]
    data = np.random.randn(1000)

    # --- 2. THE PYPLOT APPROACH (MATLAB Style) ---
    # Good for quick scripts
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label='Sine Wave', color='blue', linestyle='--')
    plt.title('Approach 1: Pyplot (Procedural)')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    # plt.show() # Uncomment to show individually

    # --- 3. OBJECT-ORIENTED APPROACH (Recommended) ---
    # Best for complex layouts and subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Approach 2: Object-Oriented (Subplots)', fontsize=16)

    # Subplot [0, 0]: Scatter Plot
    axes[0, 0].scatter(x, np.cos(x), color='red', alpha=0.5)
    axes[0, 0].set_title('Scatter Plot')
    # axes[0, 0].grid(True)

    # Subplot [0, 1]: Bar Chart
    axes[0, 1].bar(categories, values, color='green')
    axes[0, 1].set_title('Bar Chart')

    # Subplot [1, 0]: Histogram
    axes[1, 0].hist(data, bins=30, color='purple', edgecolor='black')
    axes[1, 0].set_title('Histogram')

    # Subplot [1, 1]: Pie Chart
    axes[1, 1].pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
    axes[1, 1].set_title('Pie Chart')

    plt.tight_layout(rect=(0, 0.03, 1, 0.95))

    # --- 4. ADVANCED: 3D PLOTTING ---
    fig_3d = plt.figure(figsize=(8, 6))
    ax_3d = fig_3d.add_subplot(111, projection='3d')
    
    X, Y = np.meshgrid(np.arange(-5, 5, 0.25), np.arange(-5, 5, 0.25))
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    surf = ax_3d.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    fig_3d.colorbar(surf, shrink=0.5, aspect=5)
    ax_3d.set_title('3D Surface Plot')

    print("Plots generated successfully. Displaying now...")
    plt.show()

if __name__ == "__main__":
    demonstrate_matplotlib()
