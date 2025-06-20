import pandas as pd
import matplotlib.pyplot as plt
import os

# Function to plot data from a CSV file, skipping the first row
def plot_csv(file_path, figsize=(12, 8)):
    # Read the CSV file, skipping the first row
    data = pd.read_csv(file_path, header=None, skiprows=1)

    # Extract columns (assuming the first column is X and the second column is Y)
    x = data[0] # distance
    y = data[1] # elevation

    file_name=os.path.basename(file_path)
    save_path = os.path.join('plots/plot_elevation', f'{file_name}.png')

    # Plot the data
    plt.figure(figsize=figsize)
    plt.plot(x, y, label='Elevation Profile')
    plt.xlabel('Distance')
    plt.ylabel('Elevation')
    plt.title(f'Elevation Profile from file: {file_name}')
    plt.legend()
    plt.savefig(save_path)
    plt.show()

def plot_text(file_path, figsize=(10, 6)):
    # Read the text file, skipping the first row
    data = pd.read_csv(file_path, header=None, skiprows=1, delim_whitespace=True)

    # Extract columns (assuming the first column is X and the second column is Y)
    x = data[0] # distance
    y = data[1] # elevation

    file_name=os.path.basename(file_path)
    save_path = os.path.join('plots/plot_elevation',f'{file_name}.png')

    # Plot the data
    plt.figure(figsize=figsize)
    plt.plot(x, y, label='Elevation Profile')
    plt.xlabel('Distance')
    plt.ylabel('Elevation')
    plt.title(f'Elevation Profile from file: {file_name}')
    plt.legend()
    plt.savefig(save_path)
    plt.show()

if __name__ == "__main__":
    plot_csv('profile_wysokosciowe/2018_paths/SpacerniakGdansk.csv')
    plot_csv('profile_wysokosciowe/2018_paths/WielkiKanionKolorado.csv')
    plot_csv('profile_wysokosciowe/2018_paths/MountEverest.csv')
    plot_text('profile_wysokosciowe/2018_paths/genoa_rapallo.txt')
    plot_text('profile_wysokosciowe/2018_paths/ulm_lugano.txt')
