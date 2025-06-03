import os
import random
import numpy as np
import matplotlib.pyplot as plt

from getting_nodes import get_nodes_uniform, get_nodes_chebyshev, get_nodes_random

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



def lagrange_interpolation(points, x):
    """
    Perform Lagrange interpolation.

    Args:
        points (list of tuples): List of interpolation nodes [(x0, y0), (x1, y1), ...].
        x (float): The x-value at which to evaluate the interpolated polynomial.

    Returns:
        float: Interpolated value at x.
    """
    n = len(points)
    result = 0

    for i in range(n):
        xi, yi = points[i]
        li = 1  # Lagrange basis polynomial

        for j in range(n):
            if i != j:
                xj, _ = points[j]
                li *= (x - xj) / (xi - xj)

        result += yi * li

    return result

def plot_interpolation(data_points, num_nodes, file_path, node_distribution="uniform", interval=(-1, 1)):
    """    Plot true data and interpolated data using Lagrange interpolation.

    Args:
        data_points (list of tuples): List of true data points [(x0, y0), (x1, y1), ...].
        num_nodes (int): Number of interpolation nodes to use.
        file_path (str): Path to the data file for naming purposes.
        node_distribution (str): Type of node distribution to use:
                                "uniform" (default) - evenly spaced nodes
                                "chebyshev" - Chebyshev nodes
                                "logarithmic" - more nodes at the beginning
                                "random" - randomly selected nodes
        interval (tuple): Target interval for normalization (default: [-1, 1]).

    Returns:
        None
    """
    if num_nodes < 2:
        raise ValueError("Number of interpolation nodes must be at least 2.")

    file_name = os.path.basename(file_path)
    save_path = os.path.join('plots/plot_lagrange', f'{file_name}_nodes={num_nodes}_{node_distribution}.png')

    # Sort data points by x to ensure proper interpolation
    data_points = sorted(data_points, key=lambda p: p[0])    # Select interpolation nodes based on the specified distribution
    if node_distribution == "uniform":
        interpolation_nodes = get_nodes_uniform(data_points, num_nodes)
    elif node_distribution == "chebyshev":
        interpolation_nodes = get_nodes_chebyshev(data_points, num_nodes)
    elif node_distribution == "random":
        interpolation_nodes = get_nodes_random(data_points, num_nodes)
    else:
        raise ValueError(f"Unsupported node distribution: {node_distribution}")

    # Normalize x values to the target interval
    x_original = [p[0] for p in interpolation_nodes]
    x_normalized = normalize_to_interval(x_original, interval)
    interpolation_nodes_normalized = [(x_normalized[i], interpolation_nodes[i][1]) for i in range(len(interpolation_nodes))]

    # Generate x values for interpolation across the full range of original data
    x_values_original = np.linspace(min(data_points, key=lambda p: p[0])[0], max(data_points, key=lambda p: p[0])[0], 500)
    x_values_normalized = normalize_to_interval(x_values_original, interval)
    y_interpolated = [lagrange_interpolation(interpolation_nodes_normalized, x) for x in x_values_normalized]

    # Extract x and y values for true data
    x_true = [p[0] for p in data_points]
    y_true = [p[1] for p in data_points]

    y_min, y_max = min(y_true), max(y_true)
    y_range = y_max - y_min
    y_clip = (y_min - y_range, y_max + y_range)

    # Plot true data
    plt.figure(figsize=(12, 8))
    plt.plot(x_true, y_true, label='True Data', color='blue')

    # Plot interpolated data
    plt.plot(x_values_original, y_interpolated, label=f'Lagrange Interpolation ({num_nodes} nodes)', color='red', linestyle='--')

    # Plot the nodes used for interpolation
    node_x = [p[0] for p in interpolation_nodes]
    node_y = [p[1] for p in interpolation_nodes]
    plt.scatter(node_x, node_y, color='green', s=50, label='Interpolation Nodes')

    # Add labels, legend, and title
    plt.xlabel('Distance')
    plt.ylabel('Elevation')
    plt.title(f'True Data vs Lagrange Interpolation ({node_distribution} nodes) for {file_name}')
    plt.legend()
    plt.grid()
    plt.ylim(y_clip)
    plt.savefig(save_path)
    plt.close()  # Close the figure to avoid displaying it in interactive mode


if __name__ == '__main__':
    # Example usage with a custom dataset
    data_points = [(0, 1), (1, 3), (2, 2), (3, 5), (4, 4), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10,10),(11, 7), (12, 5), (13, 3), (14, 1)]
    plot_interpolation(data_points, num_nodes=8, interval=(-1, 1))