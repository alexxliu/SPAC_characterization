import pickle
import spac
import spac.visualization
import spac.data_utils
import matplotlib.pyplot as plt
import time

#load
file_path = "path" #update with each data set
with open(file_path, 'rb') as file:
    contents = pickle.load(file)
#feautes 

#boxplot 

#annotations 

# Measure the run time of the annotation histogram generation
start_time = time.time()

#annotations histogram visualization
fig, run_times = spac.visualization.histogram(contents, annotation="broad_cell_type")  # Replace with a valid annotation name

# Calculate and print the run time
end_time = time.time()
run_time = end_time - start_time
print(f"Annotations Run time: {run_time:.4f} seconds")

#featvanno

#annovanno

#spatial

#umap

#scatterplot