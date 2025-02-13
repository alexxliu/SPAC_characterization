import pickle
import spac
import spac.visualization
import spac.data_utils
import matplotlib.pyplot as plt
import time
import anndata as ad

#load
def load(file_path):
    print(f"Processing {file_path}...")
    #load contents from fule
    with open(file_path, 'rb') as file:
        contents = pickle.load(file)

    return contents

#feature
def feature(): 
    pass

#boxplot
def boxplot(contents, file_path):
    # Measure the run time of the annotation histogram generation
    start_time = time.time()
    
    #boxplot visualization 
    fig, run_times = spac.visualization.boxplot(contents, annotation="broad_cell_type")
    
    # Calculate the run time
    end_time = time.time()
    run_time = end_time - start_time
    
    print(f"Boxplot Run time for {file_path}: {run_time:.4f} seconds")
    return fig, run_time

#annotations 
def annotations(contents, file_path):
    # Measure the run time of the annotation histogram generation
    start_time = time.time()

    # Generate the annotations histogram visualization
    fig, run_times = spac.visualization.histogram(contents, annotation="broad_cell_type")  # Replace with a valid annotation name

    # Calculate the run time
    end_time = time.time()
    run_time = end_time - start_time

    print(f"Annotations Run time for {file_path}: {run_time:.4f} seconds")
    return fig, run_times


#featvanno
def featvanno():
    pass

#annovanno

#spatial

#umap

#scatterplot



# Define your list of file paths
file_paths = [
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_10000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_30000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_50000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_70000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_90000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_110000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_130000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_150000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_170000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_190000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_200000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_400000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_600000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_800000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_1000000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_1200000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_1400000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_1600000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_1800000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_2000000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_3000000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_4000000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_5000000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_6000000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_7000000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_8000000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_9000000.pickle",
    "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_10000000.pickle",
]

def main():
    # Loop over each file path, load the file, and process it with the  function
    for file_path in file_paths:

        contents = load(file_path)
        
        # Call each visualzation function
        fig_anno, run_times = annotations(contents, file_path)
        fig_boxplot, run_times = boxplot(contents, file_path)

        #close to save mememory, only need the times
        plt.close(fig_anno)
        plt.close(fig_boxplot)

main()