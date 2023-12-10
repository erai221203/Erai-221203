import numpy as np
import matplotlib.pyplot as plt
def calculate_mean(data):
    return np.mean(data)
def calculate_median(data):
    return np.median(data)
def calculate_mode(data):
    return np.argmax(np.bincount(data))
def calculate_standard_deviation(data):
    return np.std(data)
def calculate_percentile(data, percentile):
    return np.percentile(data, percentile)
def plot_histogram(data, title, xlabel, ylabel):
    plt.hist(data, bins='auto', color='red', alpha=0.8)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
if __name__ == "__main__":
    data = [22,18,25,30,27,24,20,22,26,29,23,21,22,35,40,5,14,10]
    print(f"Mean: {calculate_mean(data)}")
    print(f"Median: {calculate_median(data)}")
    print(f"Mode: {calculate_mode(data)}")
    print(f"Standard Deviation: {calculate_standard_deviation(data)}")
    percentiles = [25, 50, 75]
    for p in percentiles:
        print(f"{p}th Percentile: {calculate_percentile(data, p)}")
    plot_histogram(data, "Data Distribution", "Value", "Frequency")
