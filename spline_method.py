import os
import numpy as np
import matplotlib.pyplot as plt

from getting_nodes import get_nodes_uniform, get_nodes_chebyshev

def normalize_to_interval(x, interval):
    """
    Normalize x values to a given interval.

    Args:
        x (list of float): Original x values.
        interval (tuple): Target interval (min, max).

    Returns:
        list of float: Normalized x values.
    """
    x_min, x_max = min(x), max(x)
    target_min, target_max = interval
    return [(target_min + (xi - x_min) * (target_max - target_min) / (x_max - x_min)) for xi in x]

def cubic_spline_coefficients(points):
    """
    Calculate the coefficients for cubic spline interpolation.
    
    Args:
        points (list of tuples): List of interpolation nodes [(x0, y0), (x1, y1), ...].
    
    Returns:
        tuple: Lists of coefficients (a, b, c, d) for each segment of the spline.
    """
    n = len(points) - 1
    
    # Extract x and y coordinates
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    
    # Calculate h (distances between consecutive x values)
    h = [x[i+1] - x[i] for i in range(n)]
    
    # Initialize the tridiagonal system
    A = np.zeros((n+1, n+1))
    B = np.zeros(n+1)
    
    # Fill the system matrix and vector
    # Natural spline boundary conditions: second derivatives at endpoints are zero
    A[0, 0] = 1.0
    A[n, n] = 1.0
    
    for i in range(1, n):
        A[i, i-1] = h[i-1]
        A[i, i] = 2 * (h[i-1] + h[i])
        A[i, i+1] = h[i]
        
        B[i] = 3 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1])
    
    # Solve the system for c coefficients
    c = np.linalg.solve(A, B)
    
    # Calculate a, b, and d coefficients
    a = y[:-1]
    b = [(y[i+1] - y[i]) / h[i] - h[i] * (2 * c[i] + c[i+1]) / 3 for i in range(n)]
    d = [(c[i+1] - c[i]) / (3 * h[i]) for i in range(n)]
    
    return a, b, c[:-1], d

def cubic_spline_interpolation(points, x):
    """
    Perform cubic spline interpolation.

    Args:
        points (list of tuples): List of interpolation nodes [(x0, y0), (x1, y1), ...].
        x (float): The x-value at which to evaluate the interpolated spline.

    Returns:
        float: Interpolated value at x.
    """
    # Sort points by x-coordinates
    points = sorted(points, key=lambda p: p[0])
    
    # Extract x coordinates
    x_nodes = [p[0] for p in points]
    
    # Check if x is outside the interpolation range
    if x < x_nodes[0] or x > x_nodes[-1]:
        raise ValueError(f"Value {x} is outside the interpolation range [{x_nodes[0]}, {x_nodes[-1]}]")
    
    # Find the appropriate segment
    i = 0
    while i < len(x_nodes) - 1 and x > x_nodes[i+1]:
        i += 1
    
    # Get spline coefficients
    a, b, c, d = cubic_spline_coefficients(points)
    
    # Calculate local coordinate
    t = x - x_nodes[i]
    
    # Evaluate the cubic polynomial
    return a[i] + b[i] * t + c[i] * t**2 + d[i] * t**3

def plot_interpolation_spline(data_points, num_nodes, file_path, node_distribution="uniform", interval=(-1, 1)):
    """
    Plot true data and interpolated data using cubic spline interpolation.

    Args:
        data_points (list of tuples): List of true data points [(x0, y0), (x1, y1), ...].
        num_nodes (int): Number of interpolation nodes to use.
        file_path (str): Path to the data file for naming purposes.
        node_distribution (str): Type of node distribution to use:
                                "uniform" (default) - evenly spaced nodes
                                "chebyshev" - Chebyshev nodes
        interval (tuple): Target interval for normalization (default: [-1, 1]).

    Returns:
        None
    """
    if num_nodes < 4:
        raise ValueError("Number of interpolation nodes must be at least 4 for cubic splines.")

    file_name = os.path.basename(file_path)+ '_spline'
    save_path = os.path.join('plots/plot_spline', f'{file_name}_nodes={num_nodes}_{node_distribution}.png')

    # Ensure plots/plot_spline directory exists
    os.makedirs('plots/plot_spline', exist_ok=True)

    # Sort data points by x to ensure proper interpolation
    data_points = sorted(data_points, key=lambda p: p[0])
    
    # Select interpolation nodes based on the specified distribution
    if node_distribution == "uniform":
        interpolation_nodes = get_nodes_uniform(data_points, num_nodes)
    elif node_distribution == "chebyshev":
        interpolation_nodes = get_nodes_chebyshev(data_points, num_nodes)
    else:
        raise ValueError(f"Unsupported node distribution: {node_distribution}")

    # Normalize x values to the target interval
    x_original = [p[0] for p in interpolation_nodes]
    x_normalized = normalize_to_interval(x_original, interval)
    interpolation_nodes_normalized = [(x_normalized[i], interpolation_nodes[i][1]) for i in range(len(interpolation_nodes))]

    # Generate x values for interpolation across the full range of original data
    x_values_original = np.linspace(min(data_points, key=lambda p: p[0])[0], max(data_points, key=lambda p: p[0])[0], 500)
    x_values_normalized = normalize_to_interval(x_values_original, interval)

    # Perform the interpolation
    y_interpolated = []
    for x in x_values_normalized:
        try:
            y_interpolated.append(cubic_spline_interpolation(interpolation_nodes_normalized, x))
        except ValueError:
            # Handle points outside interpolation range
            y_interpolated.append(np.nan)

    # Extract x and y values for true data
    x_true = [p[0] for p in data_points]
    y_true = [p[1] for p in data_points]

    y_min, y_max = min(y_true), max(y_true)
    y_range = y_max - y_min
    y_clip = (y_min - y_range, y_max + y_range)

    # Plot true data
    plt.figure(figsize=(10, 6))
    plt.plot(x_true, y_true, label='True Data', color='blue')

    # Plot interpolated data
    plt.plot(x_values_original, y_interpolated, label=f'Cubic Spline Interpolation ({num_nodes} nodes)', color='red', linestyle='--')

    # Plot the nodes used for interpolation
    node_x = [p[0] for p in interpolation_nodes]
    node_y = [p[1] for p in interpolation_nodes]
    plt.scatter(node_x, node_y, color='green', s=50, label='Interpolation Nodes')

    # Add labels, legend, and title
    plt.xlabel('Distance')
    plt.ylabel('Elevation')
    plt.title(f'True Data vs Cubic Spline Interpolation ({node_distribution} nodes) for {file_name}')
    plt.legend()
    plt.grid()
    plt.ylim(y_clip)
    plt.savefig(save_path)
    plt.close()  # Close the figure to avoid displaying it in interactive mode


if __name__ == '__main__':
    # Example usage with a custom dataset
    data_points = [(0, 1), (1, 3), (2, 2), (3, 5), (4, 4), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10,10),(11, 7), (12, 5), (13, 3), (14, 1)]
    plot_interpolation_spline(data_points, num_nodes=8, file_path='example_data', interval=(-1, 1))