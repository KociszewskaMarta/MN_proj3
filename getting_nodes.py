import random

import numpy as np


def get_nodes_uniform(data_points, num_nodes):
    """
    Select interpolation nodes uniformly across data points.

    Args:
        data_points (list of tuples): List of data points [(x0, y0), (x1, y1), ...].
        num_nodes (int): Number of interpolation nodes to use.

    Returns:
        list of tuples: Selected interpolation nodes.
    """
    indices = np.linspace(0, len(data_points) - 1, num_nodes, dtype=int)
    return [data_points[i] for i in indices]


def get_nodes_chebyshev(data_points, num_nodes):
    """
    Select interpolation nodes based on Chebyshev points.

    Args:
        data_points (list of tuples): List of data points [(x0, y0), (x1, y1), ...].
        num_nodes (int): Number of interpolation nodes to use.

    Returns:
        list of tuples: Selected interpolation nodes.
    """
    # Calculate Chebyshev nodes in interval [0, 1]
    k = np.arange(num_nodes)
    chebyshev_points = 0.5 * (1 + np.cos((2 * k + 1) * np.pi / (2 * num_nodes)))

    # Map to indices in our dataset
    max_idx = len(data_points) - 1
    indices = [int(round(p * max_idx)) for p in chebyshev_points]

    # Ensure no duplicate indices
    indices = sorted(set(indices))

    # If we lost some points due to duplicates or rounding, add more
    while len(indices) < num_nodes and max(indices) < max_idx:
        missing = num_nodes - len(indices)
        additional = np.linspace(0, max_idx, missing + 2)[1:-1]
        candidates = [int(round(a)) for a in additional if int(round(a)) not in indices]
        indices.extend(candidates[:missing])
        indices = sorted(set(indices))

    # Ensure we have exactly num_nodes points
    if len(indices) > num_nodes:
        # Remove random elements to get exactly num_nodes
        indices = sorted(random.sample(indices, num_nodes))
    elif len(indices) < num_nodes:
        # Add unique random indices until we have enough
        while len(indices) < num_nodes:
            idx = random.randint(0, max_idx)
            if idx not in indices:
                indices.append(idx)
        indices.sort()

    return [data_points[i] for i in indices]


def get_nodes_logarithmic(data_points, num_nodes):
    """
    Select interpolation nodes with logarithmic distribution (more points at the beginning).

    Args:
        data_points (list of tuples): List of data points [(x0, y0), (x1, y1), ...].
        num_nodes (int): Number of interpolation nodes to use.

    Returns:
        list of tuples: Selected interpolation nodes.
    """
    max_idx = len(data_points) - 1
    # Use logarithmic spacing
    if num_nodes > 1:
        log_space = np.logspace(0, 1, num_nodes) - 1  # from 0 to 9
        normalized = log_space / max(log_space)  # normalize to [0, 1]
        indices = [int(round(idx * max_idx)) for idx in normalized]
        indices = sorted(set(indices))  # Remove duplicates

        # Ensure we have exactly num_nodes points
        if len(indices) < num_nodes:
            # Add unique indices until we have enough
            while len(indices) < num_nodes:
                idx = random.randint(0, max_idx)
                if idx not in indices:
                    indices.append(idx)
            indices.sort()
    else:
        indices = [0]

    return [data_points[i] for i in indices]


def get_nodes_random(data_points, num_nodes):
    """
    Select interpolation nodes randomly.

    Args:
        data_points (list of tuples): List of data points [(x0, y0), (x1, y1), ...].
        num_nodes (int): Number of interpolation nodes to use.

    Returns:
        list of tuples: Selected interpolation nodes.
    """
    max_idx = len(data_points) - 1
    indices = sorted(random.sample(range(max_idx + 1), min(num_nodes, max_idx + 1)))
    return [data_points[i] for i in indices]