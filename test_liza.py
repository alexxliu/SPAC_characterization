import pickle
import spac
import importlib
import spac.visualization  # Import the module
import spac.data_utils
import matplotlib.pyplot as plt

#### Import Data Using Pickle
file_path = "dev_example.pickle"

with open(file_path, 'rb') as file:
    contents = pickle.load(file)

print(contents)

# print(contents.obs)

# print("BREAK")

# Check the unique labels in 'broad_cell_type'
print(contents.obs['broad_cell_type'].value_counts())

label_color_dict = {
    'T Cells': 'green',
    'B Cells': 'blue',
    'Other Cells': 'orange'
}



color_map_name = '_spac_colors'
label_matches, result_str = spac.data_utils.add_pin_color_rules(
    contents, label_color_dict=label_color_dict, color_map_name=color_map_name
)

print(contents)
### Selecting first and second column for X and Y datasets for Scatterplot
X_data = contents.X[:, 0]
Y_data = contents.X[:, 1]

### Run SPAC Visualization
# Ensure that we use 'broad_cell_type' for the color representation
fig, ax = spac.visualization.visualize_2D_scatter(
    x=X_data, y=Y_data, adata=contents, color_representation='broad_cell_type'
)

### Save the plot
plt.savefig('test_fig1.png')
