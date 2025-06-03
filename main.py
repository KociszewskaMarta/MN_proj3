from lagrange_method import plot_interpolation
import os

def extract_data(file_path):
    """
    Extract data from a file and return it as a list of tuples.
    Parameters
    ----------
    file_path : str
        Path to the file containing data.

    Returns
    -------
        List of tuples
    """
    data = []
    with open(file_path, 'r') as file:
        # Skip the first line
        next(file)
        for line in file:
            # Determine delimiter based on file extension
            delimiter = ',' if file_path.endswith('.csv') else None  # None for whitespace
            parts = line.strip().split(delimiter)
            if len(parts) >= 2:
                try:
                    x = float(parts[0])
                    y = float(parts[1])
                    data.append((x, y))
                except ValueError:
                    continue  # Skip lines that can't be converted to float
    return data


def ensure_directory_exists(directory_path):
    """
    Ensure that a directory exists, creating it if necessary.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def analyze_node_distribution(route, file_path, num_nodes=10):
    """
    Analyze the effect of different node distributions on interpolation.
    
    Args:
        route (list of tuples): List of data points [(x0, y0), (x1, y1), ...].
        file_path (str): Path to the data file for naming purposes.
        num_nodes (int): Number of nodes to use for interpolation.
    """
    distributions = ["uniform","chebyshev", "logarithmic", "random"]
    
    for dist in distributions:
        plot_interpolation(route, num_nodes=num_nodes, file_path=file_path, node_distribution=dist)

def analyze_route(route, file_path):
    """
    Analyze a route by plotting its elevation profile.

    Args:
        route (list of tuples): List of data points [(x0, y0), (x1, y1), ...].
        file_path (str): Path to the data file for naming purposes.
    """
    analyze_node_distribution(route,file_path, num_nodes=5)
    analyze_node_distribution(route, file_path, num_nodes=10)
    analyze_node_distribution(route, file_path, num_nodes=15)


if __name__ == "__main__":
    # Ensure directories exist
    ensure_directory_exists('plots/plot_lagrange')
    ensure_directory_exists('plots/plot_elevation')

    # Load route data
    route_SpacerniakGdansk = extract_data('profile_wysokosciowe/2018_paths/SpacerniakGdansk.csv')
    route_WielkiKanionKolorado = extract_data('profile_wysokosciowe/2018_paths/WielkiKanionKolorado.csv')
    route_MountEverest = extract_data('profile_wysokosciowe/2018_paths/MountEverest.csv')
    route_genoa_rapallo = extract_data('profile_wysokosciowe/2018_paths/genoa_rapallo.txt')
    route_ulm_lugano = extract_data('profile_wysokosciowe/2018_paths/ulm_lugano.txt')


    analyze_route(route_SpacerniakGdansk, file_path='profile_wysokosciowe/2018_paths/SpacerniakGdansk.csv')

