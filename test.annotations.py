import pickle
import spac
import spac.visualization
import matplotlib.pyplot as plt
import time  # Import time module

# Load the dataset
file_path = "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_10000000.pickle"
with open(file_path, 'rb') as file:
    contents = pickle.load(file)

# Check contents (debugging)
print(contents)

# Create an AnnData object (assuming contents.X is a numpy array and `contents.obs` contains annotations)
import anndata as ad
adata = ad.AnnData(X=contents.X, obs=contents.obs)  # Adjust as needed for proper annotations

# Select first and second column for X and Y datasets for Scatterplot (if needed)
X_data = contents.X[:, 0]
Y_data = contents.X[:, 1]

# Measure the run time of the annotation histogram generation
start_time = time.time()

# We are assuming you want a histogram visualization
fig, run_times = spac.visualization.histogram(adata, annotation="broad_cell_type")  # Replace with a valid annotation name

# Calculate and print the run time
end_time = time.time()
run_time = end_time - start_time
print(f"Annotations Run time: {run_time:.4f} seconds")