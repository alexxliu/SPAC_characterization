import pickle
import spac
import spac.visualization
import spac.data_utils
import matplotlib.pyplot as plt

#### Import Data Using Pickle (may take some research to figure out how to load it using pickle, I am actively searching out how as well.)
file_path="dev_example.pickle"

with open(file_path, 'rb') as file:
    contents = pickle.load(file)

print(contents)

### Selecting first and second column for X and Y datasets for Scatterplot

X_data = contents.X[:, 0]
Y_data = contents.X[:, 1]


### Run SPAC Visualization

#We know from the SPAC documentation it returns both a figure and set of axes
fig, ax = spac.visualization.visualize_2D_scatter(x=X_data, y=Y_data)

### Save the plot (from the SPAC manual we know its a matplotlib figure, so then I used ChatGPT to find how to display and save that figure type)
plt.savefig('test_fig1.png')



