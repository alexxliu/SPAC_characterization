import pickle
import spac
import spac.visualization
import spac.data_utils
import matplotlib.pyplot as plt

#load

def load_anndata(file_path):
    """Load AnnData object from a pickle file"""
    with open(file_path, "rb") as f:
        anndata = pickle.load(f)
    return anndata
file_path = "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_10000.pickle"
data = load_anndata(file_path)
data.obs

#feature

#boxplot

#annotations
def annotations(data, annotation):
    """Generate a histogram using spac.visualization.histogram"""
    fig, run_times = spac.visualization.histogram(data, annotation=annotation)
    plt.show()  # Ensure the plot is displayed
    return fig, run_times

annotation = "broad_cell_type"  # Replace with your annotation column name

# Call the annotations function
fig, run_times = annotations(data, annotation)

# Print run time
print("Run time:", run_times)

#featvanno

#annovanno

#spatial

#umap

#scatterplot