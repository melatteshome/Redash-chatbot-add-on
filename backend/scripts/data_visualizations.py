import matplotlib.pyplot as plt
import numpy as np


def plot_outliers(data, outlier_indices):
    data = np.array(data)
    
    # Plot the data using scatter plots
    plt.scatter(range(len(data)), data)
    plt.scatter(outlier_indices, data[outlier_indices], color='red', label='Outliers')
    plt.xlabel('Index')
    plt.ylabel('Data')
    plt.legend()
    plt.show()